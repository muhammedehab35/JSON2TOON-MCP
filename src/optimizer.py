"""
Smart Optimizer for JSON2TOON
Automatic optimization with profile-based strategies.
"""

import json
from typing import Any, Dict
from enum import Enum

from .advanced_converter import AdvancedTOONConverter, CompressionLevel
from .pattern_analyzer import AdvancedPatternAnalyzer


class OptimizationProfile(Enum):
    """Optimization profiles for different use cases."""
    SPEED = "speed"          # Fast compression, minimal processing
    BALANCED = "balanced"    # Balance between speed and compression
    SIZE = "size"            # Maximum compression, slower


class SmartOptimizer:
    """
    Intelligent optimizer that automatically selects the best strategy.
    """

    def __init__(self):
        """Initialize smart optimizer."""
        self.analyzer = AdvancedPatternAnalyzer()

    def optimize(self, data: Any, profile: str = "balanced") -> Dict[str, Any]:
        """
        Automatically optimize data with the best strategy.

        Args:
            data: JSON data to optimize
            profile: Optimization profile (speed, balanced, size)

        Returns:
            Dictionary with optimized data and metadata
        """
        # Parse profile
        try:
            opt_profile = OptimizationProfile(profile.lower())
        except ValueError:
            opt_profile = OptimizationProfile.BALANCED

        # Analyze patterns
        strategy = self.analyzer.get_compression_strategy(data)

        # Select compression level based on profile and strategy
        level = self._select_level(opt_profile, strategy.expected_savings)

        # Convert with selected level
        converter = AdvancedTOONConverter(level=level)
        original_json = json.dumps(data)
        toon_result = converter.json_to_toon(data)
        metrics = converter.calculate_metrics(original_json, toon_result)

        return {
            "toon_format": toon_result,
            "profile_used": opt_profile.value,
            "level_selected": level.name,
            "metrics": {
                "original_size": metrics.original_size,
                "compressed_size": metrics.compressed_size,
                "savings_percent": metrics.savings_percent,
                "compression_ratio": metrics.compression_ratio
            },
            "strategy": {
                "schema_compression": strategy.use_schema_compression,
                "reference_compression": strategy.use_reference_compression,
                "string_dictionary": strategy.use_string_dictionary,
                "value_compression": strategy.use_value_compression
            },
            "reasoning": strategy.reasoning
        }

    def _select_level(self, profile: OptimizationProfile, expected_savings: float) -> CompressionLevel:
        """Select optimal compression level based on profile and data."""
        if profile == OptimizationProfile.SPEED:
            # Prefer faster levels
            if expected_savings < 0.3:
                return CompressionLevel.MINIMAL
            else:
                return CompressionLevel.STANDARD

        elif profile == OptimizationProfile.SIZE:
            # Prefer maximum compression
            if expected_savings > 0.6:
                return CompressionLevel.EXTREME
            elif expected_savings > 0.4:
                return CompressionLevel.AGGRESSIVE
            else:
                return CompressionLevel.STANDARD

        else:  # BALANCED
            # Balance speed and size
            if expected_savings < 0.25:
                return CompressionLevel.MINIMAL
            elif expected_savings < 0.5:
                return CompressionLevel.STANDARD
            elif expected_savings < 0.65:
                return CompressionLevel.AGGRESSIVE
            else:
                return CompressionLevel.EXTREME
