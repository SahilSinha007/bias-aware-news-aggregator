"""
News fetching utility using NewsAPI
"""
import requests
from datetime import datetime, timedelta
from typing import List, Dict
import config

class NewsFetcher:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2"

    def fetch_news_by_topic(self, topic: str, sources: List[str] = None, 
                            max_articles: int = 5) -> Dict:
        """
        Fetch news articles for a specific topic from multiple sources

        Args:
            topic: News topic (e.g., 'technology', 'politics')
            sources: List of news sources
            max_articles: Maximum articles per source

        Returns:
            Dictionary with source as key and articles as value
        """
        if sources is None:
            sources = config.NEWS_SOURCES

        # Calculate date range (last 7 days)
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)

        all_articles = {}

        for source in sources:
            try:
                url = f"{self.base_url}/everything"
                params = {
                    'apiKey': self.api_key,
                    'q': topic,
                    'sources': source,
                    'from': start_date.strftime('%Y-%m-%d'),
                    'to': end_date.strftime('%Y-%m-%d'),
                    'language': 'en',
                    'sortBy': 'publishedAt',
                    'pageSize': max_articles
                }

                response = requests.get(url, params=params)

                if response.status_code == 200:
                    data = response.json()
                    articles = data.get('articles', [])
                    all_articles[source] = articles
                    print(f"✅ Fetched {len(articles)} articles from {source}")
                else:
                    print(f"❌ Error fetching from {source}: {response.status_code}")
                    all_articles[source] = []

            except Exception as e:
                print(f"❌ Exception for {source}: {str(e)}")
                all_articles[source] = []

        return all_articles

    def fetch_top_headlines(self, category: str = None, sources: List[str] = None) -> List[Dict]:
        """
        Fetch top headlines

        Args:
            category: News category
            sources: List of sources

        Returns:
            List of articles
        """
        url = f"{self.base_url}/top-headlines"
        params = {
            'apiKey': self.api_key,
            'language': 'en',
        }

        if category:
            params['category'] = category
        if sources:
            params['sources'] = ','.join(sources)

        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json().get('articles', [])
        except Exception as e:
            print(f"Error fetching headlines: {str(e)}")

        return []
