"""
Configuration file for the Bias-Aware News Aggregator
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY", "")
NEWS_SOURCES = os.getenv("NEWS_SOURCES", "bbc-news,cnn,fox-news,reuters,the-guardian").split(",")

# Topics
AVAILABLE_TOPICS = [
    "technology",
    "politics", 
    "sports",
    "business",
    "health",
    "entertainment"
]

# Model Configuration
SENTIMENT_MODEL = os.getenv("SENTIMENT_MODEL", "cardiffnlp/twitter-roberta-base-sentiment")
USE_VADER = os.getenv("USE_VADER", "True").lower() == "true"

# Application Settings
MAX_ARTICLES_PER_SOURCE = int(os.getenv("MAX_ARTICLES_PER_SOURCE", "5"))
CACHE_DURATION_HOURS = int(os.getenv("CACHE_DURATION_HOURS", "6"))

# Bias scoring thresholds
BIAS_THRESHOLDS = {
    "neutral": (-0.1, 0.1),
    "slight_left": (-0.3, -0.1),
    "slight_right": (0.1, 0.3),
    "left": (-0.6, -0.3),
    "right": (0.3, 0.6),
    "far_left": (-1.0, -0.6),
    "far_right": (0.6, 1.0)
}

# Source bias mapping (example - can be updated)
SOURCE_BIAS_MAP = {
    "bbc-news": 0.0,
    "reuters": 0.0,
    "cnn": -0.25,
    "fox-news": 0.35,
    "the-guardian": -0.20,
    "breitbart-news": 0.55,
    "nbc-news": -0.15,
}
