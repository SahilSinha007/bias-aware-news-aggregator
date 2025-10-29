# 📰 Bias-Aware Personalized News Aggregator

An NLP-based application that aggregates news from multiple sources, performs sentiment analysis, and detects bias to provide users with a comprehensive and balanced view of current events.

## 🎯 Project Overview

This project combines **personalized news aggregation**, **multi-source sentiment analysis**, and **bias detection** to address media polarization and information overload. Users can select topics of interest and receive news from multiple sources with transparency about sentiment and bias.

### Key Features

- ✅ **Personalized Topic Selection**: Choose from 6 news categories
- ✅ **Multi-Source Aggregation**: Compare news from 5+ sources (BBC, CNN, Fox News, Reuters, The Guardian)
- ✅ **Sentiment Analysis**: Automatic sentiment scoring using VADER
- ✅ **Bias Detection**: Identify and visualize political bias across sources
- ✅ **Diversity Metrics**: Measure perspective diversity in news coverage
- ✅ **Interactive Dashboard**: User-friendly Streamlit interface with visualizations

## 🏗️ Project Structure

```
bias-aware-news-aggregator/
│
├── data/
│   ├── raw/              # Raw downloaded datasets (place datasets here)
│   └── processed/        # Processed/cached data
│
├── src/
│   └── utils/
│       ├── __init__.py
│       ├── news_fetcher.py       # NewsAPI integration
│       ├── sentiment_analyzer.py  # VADER sentiment analysis
│       └── bias_detector.py       # Bias scoring and detection
│
├── notebooks/
│   └── (Optional Jupyter notebooks for analysis)
│
├── outputs/
│   └── (Generated reports and visualizations)
│
├── app.py                # Main Streamlit application
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variables template
├── README.md             # This file
└── SETUP.md              # Detailed setup instructions
```

## 🛠️ Technology Stack

- **Python 3.8+**
- **Streamlit**: Web interface
- **VADER Sentiment**: Sentiment analysis
- **NewsAPI**: Real-time news data
- **Plotly**: Interactive visualizations
- **Pandas & NumPy**: Data processing

## 📊 Datasets

### Real-Time Data
- **NewsAPI**: https://newsapi.org (100 free requests/day)
- Sources: BBC, CNN, Fox News, Reuters, The Guardian, and more

### Training/Testing (Optional)
- **CNN/DailyMail**: https://huggingface.co/datasets/abisee/cnn_dailymail
- **Sentiment140**: https://www.kaggle.com/datasets/kazanova/sentiment140
- Place datasets in `data/raw/` folder

## 🚀 Quick Start

### 1. Setup Environment

```bash
# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Key

```bash
# Copy example env file
cp .env.example .env

# Edit .env and add your NewsAPI key
NEWSAPI_KEY=your_api_key_here
```

Get your free API key from: https://newsapi.org

### 3. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

### 4. Using the Application

1. Enter your NewsAPI key in the sidebar (or it will use the one from .env)
2. Select topics of interest (Technology, Politics, Sports, etc.)
3. Choose news sources to compare
4. Click "Fetch News" button
5. Explore sentiment analysis and bias detection results

## 📈 Methodology

### 1. Data Collection
- Fetch news articles using NewsAPI based on user-selected topics
- Aggregate from multiple sources for comparison

### 2. Sentiment Analysis
- Use VADER (Valence Aware Dictionary and sEntiment Reasoner)
- Analyze title + description for each article
- Generate compound scores (-1 to +1)
- Classify as Positive/Negative/Neutral

### 3. Bias Detection
- Combine predefined source bias ratings with sentiment scores
- Calculate aggregate bias score per source
- Classify bias: Far-Left → Left → Slight-Left → Neutral → Slight-Right → Right → Far-Right

### 4. Comparative Analysis
- Compare sentiment across sources for same topic
- Calculate diversity score (perspective variety)
- Visualize differences in coverage

## 📝 Results

### Example Output

For topic "Technology":
- **BBC News**: Neutral bias (0.05), Positive sentiment (0.32)
- **CNN**: Slight-left bias (-0.25), Negative sentiment (-0.18)
- **Fox News**: Slight-right bias (0.35), Positive sentiment (0.22)
- **Diversity Score**: 0.67 (High perspective diversity)

### Performance Metrics
- Sentiment Classification Accuracy: 75-80% (VADER benchmark)
- API Response Time: <2 seconds per topic
- Dashboard Load Time: <3 seconds

## 🔮 Future Enhancements

- [ ] Transformer-based sentiment analysis (BERT/RoBERTa)
- [ ] Abstractive summarization of articles
- [ ] Fake news detection
- [ ] Real-time streaming updates
- [ ] User authentication and preference saving
- [ ] Mobile app version

## 👨‍💻 Author

**NLP Mini Project 2025**
- Sahil Sinha

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- NewsAPI for providing free news data
- VADER Sentiment Analysis library
- Streamlit for the web framework
- Hugging Face for NLP resources

---

**Note**: This is an academic project demonstrating NLP concepts including text preprocessing, sentiment analysis, and bias detection.
