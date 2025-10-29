# 🚀 Setup and Execution Guide

## Complete Step-by-Step Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection for API calls
- NewsAPI account (free)

---

## 📦 Installation Steps

### Step 1: Download and Extract

1. Download the `bias-aware-news-aggregator.zip` file
2. Extract it to your desired location
3. Open terminal/command prompt and navigate to the project folder:

```bash
cd bias-aware-news-aggregator
```

---

### Step 2: Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

This will install:
- streamlit (web interface)
- vaderSentiment (sentiment analysis)
- newsapi-python (news fetching)
- pandas, numpy (data processing)
- plotly (visualizations)
- And other dependencies

**Installation time**: 2-3 minutes

---

### Step 3: Get NewsAPI Key

1. Go to https://newsapi.org
2. Click "Get API Key" 
3. Sign up for free account
4. Copy your API key

**Free tier includes**: 100 requests per day (sufficient for this project)

---

### Step 4: Configure API Key

**Option A: Using .env file (Recommended)**

1. Copy the example file:
```bash
cp .env.example .env
```

2. Edit `.env` file and add your API key:
```
NEWSAPI_KEY=paste_your_api_key_here
```

**Option B: Enter in the app**

You can also paste your API key directly in the web interface sidebar when you run the app.

---

## 🎯 Where to Place Datasets

### For Real-Time News (Primary Method)
**No dataset files needed!** The app fetches real-time news using NewsAPI.

### For Offline Testing (Optional)

If you downloaded optional datasets for testing:

1. **CNN/DailyMail dataset**:
   - Place in: `data/raw/cnn_dailymail/`

2. **Sentiment140 dataset**:
   - Place in: `data/raw/sentiment140/`

3. **Any custom datasets**:
   - Place in: `data/raw/`

**Note**: The main application uses live NewsAPI data, so datasets are optional.

---

## ▶️ Running the Project

### Execution Sequence

Run **ONLY ONE FILE**: `app.py`

```bash
streamlit run app.py
```

That's it! This single command:
1. Loads all modules from `src/utils/`
2. Reads configuration from `config.py`
3. Starts the web interface
4. Opens in your browser automatically

---

## 🌐 Using the Application

### Step-by-Step Usage

1. **Browser Opens**: App will open at `http://localhost:8501`

2. **Enter API Key** (if not in .env):
   - Look at the left sidebar
   - Paste your NewsAPI key in the text field

3. **Select Topics**:
   - Check boxes for topics you want (e.g., Technology, Politics)
   - Select at least 1 topic

4. **Choose Sources**:
   - Select 2-5 news sources from the dropdown
   - Recommended: bbc-news, cnn, fox-news, reuters

5. **Fetch News**:
   - Click the "🔄 Fetch News" button
   - Wait 5-10 seconds for processing

6. **View Results**:
   - Each topic appears in a separate tab
   - See sentiment scores, bias comparison, and articles

---

## 🗂️ File Execution Order

You **DO NOT** need to run files separately. Everything runs from `app.py`.

But for understanding, here's what happens internally:

```
1. app.py (main file - YOU RUN THIS)
   ↓
2. config.py (loads automatically - configurations)
   ↓
3. src/utils/__init__.py (imports modules)
   ↓
4. src/utils/news_fetcher.py (when you click "Fetch News")
   ↓
5. src/utils/sentiment_analyzer.py (analyzes fetched articles)
   ↓
6. src/utils/bias_detector.py (calculates bias scores)
   ↓
7. Results displayed in browser
```

**You only run**: `streamlit run app.py`

**Everything else**: Runs automatically

---

## 🐛 Troubleshooting

### Problem: "Module not found" error

**Solution**:
```bash
pip install -r requirements.txt --upgrade
```

### Problem: "Invalid API key" error

**Solutions**:
1. Check your API key is correct (no extra spaces)
2. Verify your NewsAPI account is activated
3. Check you haven't exceeded 100 requests/day

### Problem: "No news articles found"

**Solutions**:
1. Try different news sources
2. Check internet connection
3. Some sources may not have recent articles for all topics

### Problem: App doesn't open in browser

**Solution**:
```bash
# Manually open: http://localhost:8501
# Or specify a different port:
streamlit run app.py --server.port 8502
```

---

## 📊 Testing the Application

### Quick Test (5 minutes)

1. Select topics: "Technology" and "Business"
2. Select sources: bbc-news, cnn, reuters
3. Click "Fetch News"
4. Verify:
   - Articles appear for each source
   - Sentiment scores are shown
   - Bias chart is displayed
   - Diversity score is calculated

### Full Test (10 minutes)

1. Test all 6 topics
2. Test with 5 different sources
3. Verify comparative analysis works
4. Check article links open correctly

---

## 💾 Saving Results

Results are not permanently saved by default (session-based).

**To save results**:

Option 1: Take screenshots of the dashboard

Option 2: Add to your GitHub repository:
```bash
# Initialize git (if not already)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Bias-Aware News Aggregator"

# Push to GitHub
git remote add origin your_github_repo_url
git push -u origin main
```

---

## 📤 Submission Checklist

For your college submission:

- [ ] All files are in the project folder
- [ ] requirements.txt is present
- [ ] README.md is complete
- [ ] .env.example is included (but NOT .env with your real API key)
- [ ] Code runs without errors
- [ ] GitHub repository is public
- [ ] Repository includes screenshots in README

---

## 🎓 For Presentation

When presenting on Oct 27/30:

1. Open the app before presentation
2. Pre-fetch news for 2-3 topics
3. Explain each visualization
4. Show how bias detection works
5. Demonstrate source comparison

**Demo time**: 5-7 minutes

---

## ⚡ Performance Notes

- **First run**: May take 10-15 seconds (downloading VADER lexicon)
- **Subsequent runs**: 2-3 seconds
- **API calls**: 5-10 seconds per topic
- **Dashboard loading**: Instant after data is fetched

---

## 🆘 Need Help?

Common issues and solutions documented above. For other issues:

1. Check all dependencies are installed
2. Verify Python version (3.8+)
3. Ensure internet connection is stable
4. Try restarting the Streamlit server

---

**Good luck with your project! 🎉**
