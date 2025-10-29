"""
Bias detection utility
"""
from typing import Dict, List
import config

class BiasDetector:
    def __init__(self):
        self.source_bias_map = config.SOURCE_BIAS_MAP
        self.bias_thresholds = config.BIAS_THRESHOLDS

    def calculate_bias_score(self, source: str, sentiment_score: float) -> float:
        """
        Calculate bias score combining source bias and sentiment

        Args:
            source: News source name
            sentiment_score: Sentiment compound score

        Returns:
            Bias score (-1 to 1)
        """
        # Get predefined source bias
        source_bias = self.source_bias_map.get(source, 0.0)

        # Combine with sentiment (weighted)
        bias_score = (source_bias * 0.7) + (sentiment_score * 0.3)

        # Clamp to -1, 1 range
        return max(-1.0, min(1.0, bias_score))

    def get_bias_label(self, bias_score: float) -> str:
        """
        Convert bias score to label

        Args:
            bias_score: Numerical bias score

        Returns:
            Bias label (e.g., 'neutral', 'left', 'right')
        """
        for label, (min_val, max_val) in self.bias_thresholds.items():
            if min_val <= bias_score < max_val:
                return label
        return 'neutral'

    def compare_sources(self, source_data: Dict) -> Dict:
        """
        Compare bias across multiple sources

        Args:
            source_data: Dictionary with source as key and sentiment stats as value

        Returns:
            Comparison results
        """
        comparisons = {}

        for source, stats in source_data.items():
            sentiment_score = stats.get('avg_compound', 0.0)
            bias_score = self.calculate_bias_score(source, sentiment_score)
            bias_label = self.get_bias_label(bias_score)

            comparisons[source] = {
                'sentiment_score': sentiment_score,
                'bias_score': round(bias_score, 3),
                'bias_label': bias_label,
                'article_count': stats.get('article_count', 0),
                'dominant_sentiment': stats.get('dominant_sentiment', 'neutral')
            }

        return comparisons

    def get_diversity_score(self, comparisons: Dict) -> float:
        """
        Calculate diversity score (how varied are the sources)

        Args:
            comparisons: Source comparison data

        Returns:
            Diversity score (0 to 1, higher is more diverse)
        """
        if len(comparisons) < 2:
            return 0.0

        bias_scores = [data['bias_score'] for data in comparisons.values()]

        # Calculate standard deviation as diversity measure
        mean_bias = sum(bias_scores) / len(bias_scores)
        variance = sum((x - mean_bias) ** 2 for x in bias_scores) / len(bias_scores)
        std_dev = variance ** 0.5

        # Normalize to 0-1 range (assuming max std_dev of 0.7)
        diversity_score = min(1.0, std_dev / 0.7)

        return round(diversity_score, 3)
