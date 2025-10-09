# 🤖 GitHub Copilot Analytics Dashboard

## 🚀 **Key Value Proposition**

**The most important value of this tool: Instant GitHub Copilot analytics without any API dependencies!**

✨ **Zero Configuration Analytics** - Simply export your users and usage data from GitHub, drop the files, and visualize comprehensive insights immediately. No API keys, no complex setup, no external dependencies.

🎯 **Core Benefits:**
- **📥 Plug & Play**: Export from GitHub → Upload files → Get instant charts
- **🚫 No APIs Required**: Works completely offline with your exported data
- **⚡ Lightning Fast**: Lightweight tool that loads and analyzes data in seconds
- **🎨 Rich Visualizations**: Professional dashboard with interactive charts and insights

### Prerequisites
- Python 3.6+ (for local server)
- Modern web browser
- GitHub Copilot usage export files (users CSV + usage JSON)

### Quick Setup & Run
```bash
git clone [repository-url]
cd github-copilot-analytics
python server.py
# Open http://localhost:8081 and upload your GitHub exports
```

**That's it! No configuration, no API setup, no complex dependencies. Just upload and visualize.**

---

A comprehensive analytics dashboard for monitoring and analyzing GitHub Copilot usage patterns across your organization.

## ✨ Features

### 📊 **Interactive Dashboard**
- **Dark Theme**: GitHub-style dark interface with monospace fonts (JetBrains Mono, Fira Code)
- **Chart Expansion**: Full-screen view of any chart with ⛶ button - click to expand, ESC to close
- **Real-time Data**: Live analytics from GitHub Copilot usage logs
- **Responsive Design**: Works seamlessly on all screen sizes

### 📈 **Analytics & Visualizations**
- **Daily Usage Trends**: Track user interactions and code generation over time
- **User Activity Rankings**: AI-powered scoring system for user engagement
- **IDE Distribution**: See which development environments are most popular
- **Feature Usage**: Monitor completion rates and acceptance patterns
- **Programming Language Analytics**: Language-specific usage insights
- **Model Usage Statistics**: AI model performance and adoption metrics

### � **User Management**
- **Active Users Page**: Ranked list of most engaged users with AI scoring
- **Inactive Users Detection**: Identify users who need encouragement
- **Smart Search**: Find users quickly with real-time filtering
- **User Display Names**: Map GitHub usernames to real names from CSV files

### 📁 **Data Management**
- **File Upload Interface**: Easy drag-and-drop data upload with real-time preview
- **Real Data Preview**: Comprehensive preview with statistics (total records, unique users, date range)
- **Format Support**: JSON, JSONL, and CSV file formats
- **Automatic Detection**: Smart file format recognition and validation

## � Quick Start

### Prerequisites
- Python 3.6+
- Modern web browser

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/github-copilot-analytics.git
   cd github-copilot-analytics
   ```

2. **Start the server:**
   ```bash
   python server.py
   ```

3. **Open your browser:**
   - Main Dashboard: http://localhost:8081/index.html
   - Data Manager: http://localhost:8081/data-manager.html
   - Active Users: http://localhost:8081/active-users.html
   - Inactive Users: http://localhost:8081/inactive-users.html

## � Data Structure

### Usage Data (JSON/JSONL)
```json
{
  "day": "2025-10-08",
  "user_id": "user123",
  "user_initiated_interaction_count": 45,
  "code_generation_activity_count": 32,
  "code_acceptance_activity_count": 28,
  "totals_by_ide": [...],
  "totals_by_language_feature": [...],
  "used_agent": true,
  "used_chat": true
}
```

### User Data (CSV)
```csv
user_id,display_name,email
user123,"John Doe",john.doe@company.com
```

## 🎨 Key Features Showcase

### � **Chart Expansion**
- Click the **⛶** button on any chart for full-screen view
- Use **ESC** key or **✕ Close** button to exit
- Responsive scaling for optimal viewing experience
- Works with all chart types (line, bar, doughnut, pie)

### 🌙 **Dark Theme**
- GitHub-inspired dark color scheme (#0d1117 background)
- Monospace fonts for better code readability
- High contrast colors (#c9d1d9 text, #58a6ff accents)
- Consistent styling across all pages

### 📊 **Interactive Data Preview**
- Real-time file analysis and statistics
- Sample data tables showing first 10 entries
- File validation and error handling
- Support for large datasets with performance optimization

### 🔄 **AI User Scoring**
Advanced algorithm that calculates user engagement scores based on:
- Interaction frequency and patterns
- Code generation and acceptance rates
- Feature adoption (agent, chat usage)
- Productivity metrics (lines added/deleted)

## 🛠️ Technical Stack

- **Frontend**: HTML5, CSS3, JavaScript ES6
- **Charts**: Chart.js with custom dark theme configuration
- **Backend**: Python HTTP server with multipart file upload support
- **Data Processing**: Client-side JSON/CSV parsing with error handling
- **Styling**: Custom CSS with CSS Grid, Flexbox, and responsive design
- **Typography**: Monospace font stack (JetBrains Mono, Fira Code, Source Code Pro, Consolas)

## 📊 Pages Overview

### Main Dashboard (`index.html`)
- Interactive charts with expansion capability
- Real-time statistics and KPIs
- Date range filtering and user search
- Export functionality for charts and data

### Data Manager (`data-manager.html`)
- File upload interface with drag-and-drop
- Real-time data preview with statistics
- File validation and format detection
- Navigation to dashboard with selected files

### Active Users (`active-users.html`)
- AI-scored user rankings (High→Low)
- Search and sort functionality
- User engagement metrics
- Interactive user cards with detailed stats

### Inactive Users (`inactive-users.html`)
- Detection of users with no activity
- User information display with CSV mapping
- Easy identification of users needing support
- Clean, organized user listing

## 🎯 AI Scoring Algorithm

The dashboard includes a sophisticated AI scoring system:

```javascript
const aiScore = (
  interactions * 0.3 +
  generations * 0.25 +
  acceptances * 0.2 +
  (usedAgent ? 15 : 0) +
  (usedChat ? 10 : 0) +
  Math.min(linesAdded / 100, 10)
);
```

Factors:
- **30%** - User interactions frequency
- **25%** - Code generation activity
- **20%** - Code acceptance rate
- **15 pts** - Agent usage bonus
- **10 pts** - Chat usage bonus
- **Up to 10 pts** - Productivity bonus (lines added)

## � Configuration

### Server Settings
- **Port**: 8081 (configurable in `server.py`)
- **Upload Limits**: No size restrictions (configurable)
- **CORS**: Enabled for all origins
- **File Types**: JSON, JSONL, CSV supported

### Chart Customization
All charts support dark theme with customizable:
- Colors and gradients
- Font families and sizes
- Animation settings
- Responsive breakpoints

## 🚧 File Structure

```
github-copilot-analytics/
├── server.py              # Python HTTP server
├── index.html             # Main dashboard
├── active-users.html      # Active users ranking
├── inactive-users.html    # Inactive users list
├── data-manager.html      # File upload and management
├── raw-data-viewer.html   # Raw data inspection
├── README.md              # This file
└── data/                  # Data directory
    ├── usage/             # Usage JSON/JSONL files
    └── users/             # User CSV files
```

## � Troubleshooting

### Charts Not Displaying
- Check browser console for JavaScript errors
- Ensure Chart.js CDN is accessible
- Verify data format matches expected structure

### File Upload Issues
- Check file format (JSON, JSONL, CSV)
- Ensure server is running on port 8081
- Verify CORS headers are enabled

### Expansion Modal Not Working
- Ensure Chart.js is loaded before page scripts
- Check for JavaScript errors in console
- Verify modal HTML elements exist

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **Chart.js** for excellent charting capabilities
- **GitHub** for Copilot usage data structure
- **JetBrains** for monospace font inspiration
- The open source community for continuous inspiration

---

**Built with ❤️ for better GitHub Copilot analytics and team productivity insights**