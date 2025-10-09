# 🌐 Project Language Guidelines

## ✅ ALWAYS USE ENGLISH

This project is 100% English language. All user-facing content must be in English.

### 📋 Content Types to Keep in English:

#### 🎯 **User Interface Elements**
- Page titles and headings
- Button text and labels
- Form placeholders and inputs
- Menu items and navigation
- Chart titles and axis labels
- Tooltips and help text
- Error messages and notifications

#### 📊 **Chart & Data Labels**
- Chart titles: "License Distribution", "Code Generation", "Activity Count"
- Axis labels: "Programming Languages", "Code Generation Count"
- Legend items: "High", "Medium", "Low", "Enterprise", "Not Specified"
- Metric labels: "Total Interactions", "Average AI Score", "Acceptance Rate"

#### 🔍 **Filters & Controls**
- Sort options: "By Name", "By License Type"
- Filter labels: "All Licenses", "All Scores"
- Search placeholders: "Search user (name or code)..."
- Button text: "Export to CSV", "Upload Files"

#### ⚠️ **Messages & Feedback**
- Success messages: "Data uploaded successfully"
- Error messages: "Could not load data", "File format error"
- Status indicators: "Loading...", "No results found"
- Instructions: "Drag and drop files here"

#### 💻 **Technical Terms**
- File formats: "JSON", "JSONL", "CSV"
- Chart types: "Doughnut Chart", "Bar Chart", "Line Chart"
- Features: "Chart expansion", "Full-screen view", "Real-time preview"

### ❌ NEVER USE TURKISH

Avoid these Turkish terms completely:
- ❌ "Kullanıcı" → ✅ "User"
- ❌ "Veri" → ✅ "Data" 
- ❌ "Grafik" → ✅ "Chart"
- ❌ "Lisans" → ✅ "License"
- ❌ "Aktif/İnaktif" → ✅ "Active/Inactive"
- ❌ "Yüksek/Orta/Düşük" → ✅ "High/Medium/Low"
- ❌ "Etkileşim" → ✅ "Interaction"
- ❌ "Kabul" → ✅ "Acceptance"
- ❌ "Üretim" → ✅ "Generation"

### 📝 **Code Comments Exception**
JavaScript comments can be in English for documentation:
```javascript
// Load user display names from CSV
// Calculate AI engagement score
// Filter users by license type
```

### 🎯 **Quality Check**
Before any commit, verify:
1. All UI text is in English
2. All chart labels are in English  
3. All error messages are in English
4. All button/form text is in English
5. All documentation is in English

### 🚀 **Enforcement**
- Review all changes before commit
- Test in browser to verify English UI
- Use grep to find Turkish words: `grep -r "kullanıcı\|veri\|grafik" *.html`

**Remember: This is a professional English-language project for international use!**