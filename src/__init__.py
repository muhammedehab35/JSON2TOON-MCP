"""
JSON2TOON - Advanced Token-Optimized Object Notation
A powerful MCP server for extreme JSON compression and optimization.
"""

from .advanced_converter import (
    AdvancedTOONConverter,
    convert_json_to_toon,
    convert_toon_to_json,
    CompressionLevel
)
from .pattern_analyzer import (
    AdvancedPatternAnalyzer,
    CompressionStrategy,
    PatternType
)
from .mcp_server import JSON2TOONServer
from .optimizer import (
    SmartOptimizer,
    OptimizationProfile
)

__version__ = "2.0.0"
__all__ = [
    "AdvancedTOONConverter",
    "convert_json_to_toon",
    "convert_toon_to_json",
    "CompressionLevel",
    "AdvancedPatternAnalyzer",
    "CompressionStrategy",
    "PatternType",
    "JSON2TOONServer",
    "SmartOptimizer",
    "OptimizationProfile"
]
