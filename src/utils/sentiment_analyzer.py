"""
Sentiment analysis utility using VADER and transformers
"""
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from typing import Dict, List
import config

class SentimentAnalyzer:
    def __init__(self, use_vader: bool = True):
        self.use_vader = use_vader

        if use_vader:
            self.vader = SentimentIntensityAnalyzer()
            print("✅ Loaded VADER sentiment analyzer")
        else:
            # For transformer model - can add later
            print("⚠️ Transformer model not implemented yet, using VADER")
            self.vader = SentimentIntensityAnalyzer()
            self.use_vader = True

    def analyze_text(self, text: str) -> Dict:
        """
        Analyze sentiment of text

        Args:
            text: Input text

        Returns:
            Dictionary with sentiment scores
        """
        if not text or len(text.strip()) == 0:
            return {
                'compound': 0.0,
                'positive': 0.0,
                'negative': 0.0,
                'neutral': 1.0,
                'label': 'neutral'
            }

        if self.use_vader:
            scores = self.vader.polarity_scores(text)

            # Determine label based on compound score
            compound = scores['compound']
            if compound >= 0.05:
                label = 'positive'
            elif compound <= -0.05:
                label = 'negative'
            else:
                label = 'neutral'

            scores['label'] = label
            return scores

    def analyze_article(self, article: Dict) -> Dict:
        """
        Analyze sentiment of news article

        Args:
            article: Article dictionary with 'title' and 'description'

        Returns:
            Article with sentiment scores added
        """
        # Combine title and description for analysis
        text = f"{article.get('title', '')} {article.get('description', '')}"
        sentiment = self.analyze_text(text)

        article['sentiment'] = sentiment
        return article

    def analyze_articles(self, articles: List[Dict]) -> List[Dict]:
        """
        Analyze sentiment for multiple articles

        Args:
            articles: List of article dictionaries

        Returns:
            Articles with sentiment scores
        """
        analyzed = []
        for article in articles:
            analyzed.append(self.analyze_article(article))
        return analyzed

    def get_source_sentiment_stats(self, articles: List[Dict]) -> Dict:
        """
        Calculate aggregate sentiment statistics

        Args:
            articles: List of analyzed articles

        Returns:
            Sentiment statistics
        """
        if not articles:
            return {
                'avg_compound': 0.0,
                'avg_positive': 0.0,
                'avg_negative': 0.0,
                'avg_neutral': 0.0,
                'dominant_sentiment': 'neutral'
            }

        total_compound = sum(a.get('sentiment', {}).get('compound', 0) for a in articles)
        total_pos = sum(a.get('sentiment', {}).get('pos', 0) for a in articles)
        total_neg = sum(a.get('sentiment', {}).get('neg', 0) for a in articles)
        total_neu = sum(a.get('sentiment', {}).get('neu', 0) for a in articles)

        count = len(articles)
        avg_compound = total_compound / count

        # Determine dominant sentiment
        if avg_compound >= 0.05:
            dominant = 'positive'
        elif avg_compound <= -0.05:
            dominant = 'negative'
        else:
            dominant = 'neutral'

        return {
            'avg_compound': round(avg_compound, 3),
            'avg_positive': round(total_pos / count, 3),
            'avg_negative': round(total_neg / count, 3),
            'avg_neutral': round(total_neu / count, 3),
            'dominant_sentiment': dominant,
            'article_count': count
        }
