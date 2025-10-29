"""
Bias-Aware Personalized News Aggregator
Main Streamlit Application
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import sys
sys.path.append('.')

import config
from src.utils import NewsFetcher, SentimentAnalyzer, BiasDetector

# Page configuration
st.set_page_config(
    page_title="Bias-Aware News Aggregator",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'news_data' not in st.session_state:
    st.session_state.news_data = None
if 'selected_topics' not in st.session_state:
    st.session_state.selected_topics = []

# Header
st.title("📰 Bias-Aware News Aggregator")
st.markdown("**Personalized News with Multi-Source Sentiment Analysis & Bias Detection**")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")

    # API Key input
    api_key = st.text_input(
        "NewsAPI Key", 
        type="password",
        value=config.NEWSAPI_KEY,
        help="Get your free API key from https://newsapi.org"
    )

    st.markdown("---")

    # Topic selection
    st.subheader("📋 Select Your Topics")
    selected_topics = []
    for topic in config.AVAILABLE_TOPICS:
        if st.checkbox(topic.title(), key=f"topic_{topic}"):
            selected_topics.append(topic)

    st.session_state.selected_topics = selected_topics

    st.markdown("---")

    # Source selection
    st.subheader("📡 News Sources")
    selected_sources = st.multiselect(
        "Choose sources",
        config.NEWS_SOURCES,
        default=config.NEWS_SOURCES[:3]
    )

    st.markdown("---")

    # Fetch button
    fetch_button = st.button("🔄 Fetch News", type="primary", use_container_width=True)

# Main content area
if not api_key:
    st.warning("⚠️ Please enter your NewsAPI key in the sidebar to get started.")
    st.info("Get a free API key from https://newsapi.org")
elif not selected_topics:
    st.info("👈 Please select at least one topic from the sidebar to continue.")
else:
    if fetch_button:
        with st.spinner("Fetching and analyzing news..."):
            # Initialize components
            fetcher = NewsFetcher(api_key)
            analyzer = SentimentAnalyzer(use_vader=config.USE_VADER)
            detector = BiasDetector()

            # Store results
            all_results = {}

            # Process each topic
            for topic in selected_topics:
                # Fetch news
                articles_by_source = fetcher.fetch_news_by_topic(
                    topic, 
                    selected_sources,
                    config.MAX_ARTICLES_PER_SOURCE
                )

                # Analyze sentiment for each source
                source_stats = {}
                for source, articles in articles_by_source.items():
                    if articles:
                        analyzed_articles = analyzer.analyze_articles(articles)
                        stats = analyzer.get_source_sentiment_stats(analyzed_articles)
                        source_stats[source] = stats
                        articles_by_source[source] = analyzed_articles

                # Detect bias
                bias_comparison = detector.compare_sources(source_stats)
                diversity_score = detector.get_diversity_score(bias_comparison)

                all_results[topic] = {
                    'articles': articles_by_source,
                    'stats': source_stats,
                    'bias': bias_comparison,
                    'diversity': diversity_score
                }

            st.session_state.news_data = all_results
            st.success("✅ News fetched and analyzed successfully!")

    # Display results
    if st.session_state.news_data:
        results = st.session_state.news_data

        # Create tabs for each topic
        tabs = st.tabs([topic.title() for topic in selected_topics])

        for idx, topic in enumerate(selected_topics):
            with tabs[idx]:
                if topic not in results:
                    st.warning(f"No data available for {topic}")
                    continue

                topic_data = results[topic]

                # Display diversity score
                diversity = topic_data['diversity']
                col1, col2, col3 = st.columns([2, 2, 3])
                with col1:
                    st.metric("Diversity Score", f"{diversity:.2f}")
                with col2:
                    st.metric("Sources", len(topic_data['bias']))

                st.markdown("---")

                # Bias comparison chart
                st.subheader("📊 Bias & Sentiment Comparison")

                bias_data = topic_data['bias']
                if bias_data:
                    # Create dataframe
                    df = pd.DataFrame.from_dict(bias_data, orient='index')
                    df['source'] = df.index

                    # Create chart
                    fig = go.Figure()
                    fig.add_trace(go.Bar(
                        x=df['source'],
                        y=df['bias_score'],
                        name='Bias Score',
                        marker_color=['red' if x > 0 else 'blue' if x < 0 else 'gray' 
                                      for x in df['bias_score']]
                    ))

                    fig.update_layout(
                        title="Source Bias Comparison",
                        xaxis_title="Source",
                        yaxis_title="Bias Score",
                        height=400
                    )

                    st.plotly_chart(fig, use_container_width=True)

                    # Table
                    st.subheader("📋 Detailed Analysis")
                    display_df = df[['source', 'sentiment_score', 'bias_score', 
                                     'bias_label', 'dominant_sentiment', 'article_count']]
                    st.dataframe(display_df, use_container_width=True)

                    # Articles
                    st.markdown("---")
                    st.subheader("📰 Sample Articles")

                    for source in selected_sources:
                        if source in topic_data['articles'] and topic_data['articles'][source]:
                            with st.expander(f"{source.upper()} ({len(topic_data['articles'][source])} articles)"):
                                articles = topic_data['articles'][source][:3]
                                for article in articles:
                                    sentiment = article.get('sentiment', {})
                                    st.markdown(f"**{article.get('title', 'No title')}**")
                                    st.write(f"Sentiment: {sentiment.get('label', 'neutral')} ({sentiment.get('compound', 0):.2f})")
                                    st.write(article.get('description', 'No description'))
                                    if article.get('url'):
                                        st.markdown(f"[Read more]({article['url']})")
                                    st.markdown("---")

# Footer
st.markdown("---")
st.caption("NMIMS Indore | NLP Mini Project 2025 | Data from NewsAPI")
