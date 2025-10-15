#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub Copilot Metrics Server with File Upload Support
Simple HTTP server with data visualization tools and file management
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import json
import urllib.parse
import cgi
from pathlib import Path

# Server configuration
PORT = 8081
HOST = "localhost"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP handler with CORS headers, file upload, and proper MIME types"""
    
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def guess_type(self, path):
        """Properly identify file types"""
        try:
            mimetype, encoding = super().guess_type(path)
            if path.endswith('.json'):
                return 'application/json', encoding
            elif path.endswith('.jsonl'):
                return 'application/json', encoding
            elif path.endswith('.csv'):
                return 'text/csv', encoding
            return mimetype, encoding
        except:
            if path.endswith('.json') or path.endswith('.jsonl'):
                return 'application/json', None
            elif path.endswith('.csv'):
                return 'text/csv', None
            return 'text/html', None

    def do_OPTIONS(self):
        """Handle OPTIONS requests for CORS"""
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        """Handle POST requests"""
        if self.path == '/api/upload':
            self.handle_file_upload()
        else:
            self.send_error(404, "Not Found")

    def do_GET(self):
        """Handle GET requests"""
        if self.path.startswith('/api/files/'):
            self.handle_file_list()
        else:
            super().do_GET()

    def handle_file_upload(self):
        """Handle file upload requests"""
        try:
            content_type = self.headers.get('Content-Type', '')
            if not content_type.startswith('multipart/form-data'):
                self.send_error(400, "Expected multipart/form-data")
                return

            # Parse multipart form data
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            # Simple multipart parser
            boundary = content_type.split('boundary=')[1].encode()
            parts = post_data.split(b'--' + boundary)
            
            uploaded_file = None
            file_type = None
            
            for part in parts:
                if b'Content-Disposition' in part:
                    part_str = part.decode('utf-8', errors='ignore')
                    
                    if 'name="file"' in part_str and 'filename=' in part_str:
                        # Extract filename
                        filename_start = part_str.find('filename="') + 10
                        filename_end = part_str.find('"', filename_start)
                        filename = part_str[filename_start:filename_end]
                        
                        # Extract file data
                        header_end = part.find(b'\r\n\r\n')
                        if header_end != -1:
                            file_data = part[header_end + 4:]
                            # Remove trailing boundary markers
                            if file_data.endswith(b'\r\n'):
                                file_data = file_data[:-2]
                            
                            uploaded_file = {
                                'filename': filename,
                                'data': file_data
                            }
                    
                    elif 'name="type"' in part_str:
                        # Extract file type
                        header_end = part.find(b'\r\n\r\n')
                        if header_end != -1:
                            type_data = part[header_end + 4:]
                            if type_data.endswith(b'\r\n'):
                                type_data = type_data[:-2]
                            file_type = type_data.decode('utf-8')

            if uploaded_file and file_type:
                # Validate file type and extension
                filename = uploaded_file['filename']
                if file_type == 'usage' and not (filename.endswith('.json') or filename.endswith('.jsonl')):
                    self.send_error(400, "Usage files must be .json or .jsonl")
                    return
                elif file_type == 'users' and not filename.endswith('.csv'):
                    self.send_error(400, "User files must be .csv")
                    return

                # Create upload directory
                upload_dir = Path(f'data/{file_type}')
                upload_dir.mkdir(parents=True, exist_ok=True)
                
                # Save file
                file_path = upload_dir / filename
                with open(file_path, 'wb') as f:
                    f.write(uploaded_file['data'])
                
                # Send success response
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                
                response = {
                    'success': True,
                    'message': f'File {filename} uploaded successfully',
                    'path': str(file_path).replace('\\', '/')
                }
                self.wfile.write(json.dumps(response).encode())
                
                print(f"✅ Uploaded: {filename} -> {file_path}")
            else:
                self.send_error(400, "Invalid upload data")
                
        except Exception as e:
            print(f"❌ Upload error: {e}")
            self.send_error(500, f'Upload failed: {str(e)}')

    def handle_file_list(self):
        """Handle file listing requests"""
        try:
            # Extract file type from URL (usage or users)
            path_parts = self.path.strip('/').split('/')
            if len(path_parts) >= 3:
                file_type = path_parts[2]  # api/files/usage or api/files/users
            else:
                self.send_error(400, "Invalid file list request")
                return
            
            data_dir = Path(f'data/{file_type}')
            files = []
            
            if data_dir.exists() and data_dir.is_dir():
                for file_path in data_dir.iterdir():
                    if file_path.is_file():
                        try:
                            stat = file_path.stat()
                            
                            # Format file size
                            size_bytes = stat.st_size
                            if size_bytes == 0:
                                size_str = '0 Bytes'
                            else:
                                k = 1024
                                sizes = ['Bytes', 'KB', 'MB', 'GB']
                                i = 0
                                size = size_bytes
                                while size >= k and i < len(sizes) - 1:
                                    size = size / k
                                    i += 1
                                size_str = f"{size:.2f} {sizes[i]}"
                            
                            # Get file creation/modification time
                            from datetime import datetime
                            mtime = datetime.fromtimestamp(stat.st_mtime)
                            created_date = mtime.strftime('%Y-%m-%d %H:%M')
                            
                            files.append({
                                'name': file_path.name,
                                'size': size_str,
                                'type': self.guess_type(str(file_path))[0] or 'application/octet-stream',
                                'path': str(file_path).replace('\\', '/'),
                                'uploaded': True,
                                'createdDate': created_date
                            })
                        except Exception as e:
                            print(f"⚠️  Error reading file {file_path}: {e}")
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(files).encode())
            
        except Exception as e:
            print(f"❌ File list error: {e}")
            self.send_error(500, f'Failed to list files: {str(e)}')

def check_and_create_directories():
    """Check and create necessary directories"""
    directories = ['data', 'data/usage', 'data/users']
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
    print("📁 Directory structure verified")

def start_server():
    """Start the HTTP server"""
    
    current_dir = Path.cwd()
    print(f"🚀 GitHub Copilot Metrics Server Starting...")
    print(f"📁 Working directory: {current_dir}")
    print(f"🌐 Server address: http://{HOST}:{PORT}")
    print(f"📊 Main dashboard: http://{HOST}:{PORT}/index.html")
    print(f"📋 Raw data viewer: http://{HOST}:{PORT}/raw-data-viewer.html")
    print(f"📁 Data manager: http://{HOST}:{PORT}/data-manager.html")
    print("=" * 60)
    
    # Check and create directories
    check_and_create_directories()
    
    try:
        # Start server
        with socketserver.TCPServer((HOST, PORT), CustomHandler) as httpd:
            print(f"✅ Server running at http://{HOST}:{PORT}")
            print("🔄 Press Ctrl+C to stop the server")
            print("=" * 60)
            
            # Auto-open browser
            try:
                webbrowser.open(f"http://{HOST}:{PORT}/data-manager.html")
                print("🌐 Browser opened automatically")
            except:
                print("⚠️  Could not open browser automatically")
            
            # Keep server running
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Server shutting down...")
        return True
    except OSError as e:
        if e.errno == 48 or "Address already in use" in str(e):
            print(f"❌ Port {PORT} is already in use. Try a different port.")
            return False
        else:
            print(f"❌ Server start error: {e}")
            return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def main():
    """Main function"""
    print("🤖 GitHub Copilot Usage Analytics Server")
    print("=" * 60)
    
    # Help message
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', 'help']:
        print("""
Usage:
    python server.py              # Start the server
    python server.py -h           # Show this help message

Features:
    • 📊 Interactive dashboard (index.html)
    • 📋 Raw data viewer (raw-data-viewer.html)
    • 📁 Data manager (data-manager.html)
    • 📤 File upload support
    • 📈 Chart.js visualizations
    • 🔍 Filtering and search
    • 📥 Data export

Requirements:
    • Python 3.6+
    • Data files in data/usage/ and data/users/ directories
        """)
        return
    
    # Start server
    success = start_server()
    
    if success:
        print("✅ Server shut down successfully")
    else:
        print("❌ Server shut down with errors")
        sys.exit(1)

if __name__ == "__main__":
    main()