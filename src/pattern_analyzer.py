"""
Advanced Pattern Analyzer for JSON2TOON
AI-powered pattern detection and compression strategy optimization.
"""

import re
import json
from typing import Any, Dict, List, Optional, Set, Tuple
from collections import Counter
from dataclasses import dataclass
from enum import Enum


class PatternType(Enum):
    """Types of patterns that can be detected."""
    API_RESPONSE = "api_response"
    DATABASE_RECORD = "database_record"
    USER_DATA = "user_data"
    PAGINATION = "pagination"
    NESTED_ADDRESS = "nested_address"
    NESTED_COORDINATES = "nested_coordinates"
    NESTED_DIMENSIONS = "nested_dimensions"
    NESTED_METADATA = "nested_metadata"
    HOMOGENEOUS_ARRAY = "homogeneous_array"
    CONSISTENT_SCHEMA_ARRAY = "consistent_schema_array"
    REPEATED_STRUCTURE = "repeated_structure"
    TIME_SERIES = "time_series"
    GRAPH_NODE = "graph_node"
    TREE_STRUCTURE = "tree_structure"
    ENUM_VALUES = "enum_values"
    SPARSE_ARRAY = "sparse_array"
    DEEP_NESTING = "deep_nesting"


@dataclass
class Pattern:
    """Represents a detected pattern with metadata."""
    pattern_type: PatternType
    confidence: float
    location: str
    keys: Optional[List[str]] = None
    sample: Optional[Any] = None
    count: int = 0
    compression_potential: float = 0.0
    recommendation: str = ""


@dataclass
class CompressionStrategy:
    """Recommended compression strategy for data."""
    use_schema_compression: bool
    use_reference_compression: bool
    use_string_dictionary: bool
    use_value_compression: bool
    use_partial_schema: bool
    custom_abbreviations: Dict[str, str]
    expected_savings: float
    recommended_level: int
    patterns: List[Pattern]
    reasoning: List[str]


class AdvancedPatternAnalyzer:
    """
    Advanced pattern analyzer with ML-inspired heuristics.

    Features:
    - 17+ pattern types (vs 8 in original)
    - Confidence scoring
    - Compression potential estimation
    - Context-aware recommendations
    - Deep structure analysis
    """

    # Extended pattern definitions
    API_PATTERNS = {
        'rest_response': ['status', 'data', 'message', 'meta'],
        'graphql_response': ['data', 'errors', 'extensions'],
        'json_rpc': ['jsonrpc', 'result', 'error', 'id'],
        'oauth': ['access_token', 'token_type', 'expires_in', 'refresh_token'],
        'error_response': ['error', 'error_code', 'error_message', 'details'],
    }

    DATABASE_PATTERNS = {
        'crud_record': ['id', 'created_at', 'updated_at', 'deleted_at'],
        'audit_log': ['user_id', 'action', 'timestamp', 'changes'],
        'versioned': ['id', 'version', 'created_at', 'updated_at'],
        'soft_delete': ['deleted_at', 'deleted_by', 'is_deleted'],
    }

    USER_PATTERNS = {
        'basic_user': ['username', 'email', 'password'],
        'profile': ['first_name', 'last_name', 'avatar', 'bio'],
        'authentication': ['token', 'session_id', 'expires_at'],
        'preferences': ['theme', 'language', 'timezone', 'notifications'],
    }

    NESTED_PATTERNS = {
        'address': ['street', 'city', 'state', 'postal_code', 'country'],
        'coordinates': ['latitude', 'longitude', 'altitude'],
        'dimensions': ['width', 'height', 'depth', 'unit'],
        'date_range': ['start_date', 'end_date'],
        'time_range': ['start_time', 'end_time'],
        'contact': ['email', 'phone', 'mobile', 'fax'],
        'social_links': ['facebook', 'twitter', 'linkedin', 'instagram'],
        'metadata': ['created_by', 'updated_by', 'tags', 'category'],
    }

    PAGINATION_PATTERNS = [
        'page', 'per_page', 'total_pages', 'total_count',
        'limit', 'offset', 'next', 'previous', 'has_more'
    ]

    def __init__(self):
        """Initialize advanced pattern analyzer."""
        self.detected_patterns: List[Pattern] = []
        self.key_frequency: Counter = Counter()
        self.value_type_counts: Counter = Counter()
        self.nesting_depths: List[int] = []
        self.array_sizes: List[int] = []

    def analyze(self, data: Any, path: str = "$") -> List[Pattern]:
        """
        Perform comprehensive pattern analysis.

        Args:
            data: JSON data to analyze
            path: JSONPath location (for nested analysis)

        Returns:
            List of detected patterns with confidence scores
        """
        self.detected_patterns = []
        self.key_frequency = Counter()
        self.value_type_counts = Counter()
        self.nesting_depths = []
        self.array_sizes = []

        # Deep traverse and collect statistics
        self._deep_traverse(data, path, depth=0)

        # Detect all pattern types
        self._detect_api_patterns(data, path)
        self._detect_database_patterns(data, path)
        self._detect_user_patterns(data, path)
        self._detect_nested_patterns(data, path)
        self._detect_pagination_patterns(data, path)
        self._detect_array_patterns(data, path)
        self._detect_structure_patterns(data, path)
        self._detect_time_series(data, path)
        self._detect_graph_patterns(data, path)
        self._detect_tree_patterns(data, path)
        self._detect_enum_patterns(data, path)
        self._detect_sparse_patterns(data, path)
        self._detect_deep_nesting(data, path)

        # Sort by confidence and compression potential
        self.detected_patterns.sort(
            key=lambda p: (p.confidence * p.compression_potential),
            reverse=True
        )

        return self.detected_patterns

    def _deep_traverse(self, data: Any, path: str, depth: int) -> None:
        """Deep traverse to collect comprehensive statistics."""
        self.nesting_depths.append(depth)

        if isinstance(data, dict):
            for key, value in data.items():
                self.key_frequency[key] += 1
                self.value_type_counts[type(value).__name__] += 1
                self._deep_traverse(value, f"{path}.{key}", depth + 1)

        elif isinstance(data, list):
            self.array_sizes.append(len(data))
            for i, item in enumerate(data):
                self._deep_traverse(item, f"{path}[{i}]", depth + 1)

    def _detect_api_patterns(self, data: Any, path: str) -> None:
        """Detect API-related patterns."""
        if not isinstance(data, dict):
            return

        for pattern_name, pattern_keys in self.API_PATTERNS.items():
            matches = sum(1 for key in pattern_keys if key in data)
            confidence = matches / len(pattern_keys)

            if confidence > 0.4:
                self.detected_patterns.append(Pattern(
                    pattern_type=PatternType.API_RESPONSE,
                    confidence=confidence,
                    location=path,
                    keys=[k for k in pattern_keys if k in data],
                    compression_potential=0.5 + (confidence * 0.3),
                    recommendation=f"Detected {pattern_name} pattern - use schema compression"
                ))

    def _detect_database_patterns(self, data: Any, path: str) -> None:
        """Detect database record patterns."""
        if isinstance(data, dict):
            for pattern_name, pattern_keys in self.DATABASE_PATTERNS.items():
                matches = sum(1 for key in pattern_keys if key in data)
                confidence = matches / len(pattern_keys)

                if confidence > 0.4:
                    self.detected_patterns.append(Pattern(
                        pattern_type=PatternType.DATABASE_RECORD,
                        confidence=confidence,
                        location=path,
                        keys=[k for k in pattern_keys if k in data],
                        compression_potential=0.6 + (confidence * 0.2),
                        recommendation=f"Detected {pattern_name} - highly compressible with key abbreviations"
                    ))

        elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            # Check for array of database records
            for pattern_name, pattern_keys in self.DATABASE_PATTERNS.items():
                matches = sum(1 for key in pattern_keys if key in data[0])
                confidence = matches / len(pattern_keys)

                if confidence > 0.4:
                    self.detected_patterns.append(Pattern(
                        pattern_type=PatternType.DATABASE_RECORD,
                        confidence=confidence,
                        location=path,
                        keys=[k for k in pattern_keys if k in data[0]],
                        count=len(data),
                        compression_potential=0.7 + (confidence * 0.2),
                        recommendation=f"Array of {len(data)} {pattern_name} records - excellent for schema compression"
                    ))

    def _detect_user_patterns(self, data: Any, path: str) -> None:
        """Detect user data patterns."""
        if not isinstance(data, dict):
            return

        for pattern_name, pattern_keys in self.USER_PATTERNS.items():
            matches = sum(1 for key in pattern_keys if key in data)
            confidence = matches / len(pattern_keys)

            if confidence > 0.35:
                self.detected_patterns.append(Pattern(
                    pattern_type=PatternType.USER_DATA,
                    confidence=confidence,
                    location=path,
                    keys=[k for k in pattern_keys if k in data],
                    compression_potential=0.5,
                    recommendation=f"User {pattern_name} detected - consider string dictionary for repeated values"
                ))

    def _detect_nested_patterns(self, data: Any, path: str) -> None:
        """Detect nested structure patterns."""
        if not isinstance(data, dict):
            return

        for pattern_name, pattern_keys in self.NESTED_PATTERNS.items():
            for key, value in data.items():
                if isinstance(value, dict):
                    matches = sum(1 for pk in pattern_keys if pk in value)
                    confidence = matches / len(pattern_keys)

                    if confidence > 0.6:
                        pattern_type = getattr(
                            PatternType,
                            f"NESTED_{pattern_name.upper()}",
                            PatternType.NESTED_METADATA
                        )

                        self.detected_patterns.append(Pattern(
                            pattern_type=pattern_type,
                            confidence=confidence,
                            location=f"{path}.{key}",
                            keys=[pk for pk in pattern_keys if pk in value],
                            compression_potential=0.4,
                            recommendation=f"Nested {pattern_name} - use compact object notation"
                        ))

    def _detect_pagination_patterns(self, data: Any, path: str) -> None:
        """Detect pagination patterns."""
        if not isinstance(data, dict):
            return

        matches = sum(1 for key in self.PAGINATION_PATTERNS if key in data)
        confidence = matches / len(self.PAGINATION_PATTERNS)

        if confidence > 0.3:
            self.detected_patterns.append(Pattern(
                pattern_type=PatternType.PAGINATION,
                confidence=confidence,
                location=path,
                keys=[k for k in self.PAGINATION_PATTERNS if k in data],
                compression_potential=0.3,
                recommendation="Pagination metadata - use key abbreviations"
            ))

    def _detect_array_patterns(self, data: Any, path: str) -> None:
        """Detect array patterns with advanced analysis."""
        if not isinstance(data, dict):
            return

        for key, value in data.items():
            if isinstance(value, list) and len(value) > 0:
                # Homogeneous arrays
                if self._is_homogeneous_array(value):
                    item_type = type(value[0]).__name__
                    self.detected_patterns.append(Pattern(
                        pattern_type=PatternType.HOMOGENEOUS_ARRAY,
                        confidence=1.0,
                        location=f"{path}.{key}",
                        keys=[key],
                        count=len(value),
                        compression_potential=0.5,
                        recommendation=f"Homogeneous {item_type} array - efficient for compact storage"
                    ))

                # Consistent schema arrays
                if all(isinstance(item, dict) for item in value):
                    consistency = self._calculate_schema_consistency(value)
                    if consistency > 0.7:
                        # Calculate compression potential based on size and consistency
                        size_factor = min(len(value) / 100, 1.0)  # More items = better compression
                        potential = 0.5 + (consistency * 0.3) + (size_factor * 0.2)

                        self.detected_patterns.append(Pattern(
                            pattern_type=PatternType.CONSISTENT_SCHEMA_ARRAY,
                            confidence=consistency,
                            location=f"{path}.{key}",
                            keys=[key],
                            count=len(value),
                            sample=value[0] if value else None,
                            compression_potential=min(potential, 0.9),
                            recommendation=f"Array of {len(value)} objects with {consistency:.0%} schema consistency - excellent for schema compression"
                        ))

    def _detect_structure_patterns(self, data: Any, path: str) -> None:
        """Detect repeated structure patterns."""
        structure_hashes: Counter = Counter()
        structure_samples: Dict[str, Any] = {}

        def hash_structure(obj: Any) -> Optional[str]:
            if isinstance(obj, dict):
                return '|'.join(sorted(obj.keys()))
            return None

        def collect_structures(d: Any, p: str = ""):
            if isinstance(d, dict):
                h = hash_structure(d)
                if h:
                    structure_hashes[h] += 1
                    if h not in structure_samples:
                        structure_samples[h] = (p, d)
                for k, v in d.items():
                    collect_structures(v, f"{p}.{k}")
            elif isinstance(d, list):
                for i, item in enumerate(d):
                    collect_structures(item, f"{p}[{i}]")

        collect_structures(data, path)

        # Find frequently repeated structures
        for structure, count in structure_hashes.items():
            if count >= 3:
                keys = structure.split('|')
                location, sample = structure_samples[structure]

                # Higher compression potential for more repetitions
                potential = min(0.5 + (count / 20), 0.85)

                self.detected_patterns.append(Pattern(
                    pattern_type=PatternType.REPEATED_STRUCTURE,
                    confidence=min(count / 10.0, 1.0),
                    location=location,
                    keys=keys[:5],  # First 5 keys
                    count=count,
                    compression_potential=potential,
                    recommendation=f"Structure repeated {count} times - use reference compression"
                ))

    def _detect_time_series(self, data: Any, path: str) -> None:
        """Detect time series data patterns."""
        if not isinstance(data, list) or len(data) < 5:
            return

        # Check if array contains objects with timestamp fields
        timestamp_keys = ['timestamp', 'time', 'created_at', 'date', 'datetime']
        has_timestamps = False

        if all(isinstance(item, dict) for item in data):
            for item in data[:5]:  # Check first 5 items
                if any(key in item for key in timestamp_keys):
                    has_timestamps = True
                    break

            if has_timestamps:
                self.detected_patterns.append(Pattern(
                    pattern_type=PatternType.TIME_SERIES,
                    confidence=0.8,
                    location=path,
                    count=len(data),
                    compression_potential=0.7,
                    recommendation=f"Time series with {len(data)} data points - use schema compression + delta encoding"
                ))

    def _detect_graph_patterns(self, data: Any, path: str) -> None:
        """Detect graph/node patterns."""
        if not isinstance(data, dict):
            return

        # Graph node indicators
        graph_keys = ['nodes', 'edges', 'vertices', 'connections', 'links']
        node_keys = ['id', 'neighbors', 'adjacent', 'children', 'parents']

        has_graph_structure = any(key in data for key in graph_keys)
        has_node_structure = sum(1 for key in node_keys if key in data) >= 2

        if has_graph_structure or has_node_structure:
            confidence = 0.7 if has_graph_structure else 0.5

            self.detected_patterns.append(Pattern(
                pattern_type=PatternType.GRAPH_NODE,
                confidence=confidence,
                location=path,
                compression_potential=0.6,
                recommendation="Graph structure detected - use reference compression for node relationships"
            ))

    def _detect_tree_patterns(self, data: Any, path: str) -> None:
        """Detect tree structure patterns."""
        if not isinstance(data, dict):
            return

        # Tree indicators
        tree_keys = ['children', 'parent', 'left', 'right', 'subtree']
        matches = sum(1 for key in tree_keys if key in data)

        if matches >= 1:
            # Check if children is an array
            has_children_array = isinstance(data.get('children'), list)
            confidence = 0.8 if has_children_array else 0.5

            self.detected_patterns.append(Pattern(
                pattern_type=PatternType.TREE_STRUCTURE,
                confidence=confidence,
                location=path,
                compression_potential=0.55,
                recommendation="Tree structure - use recursive compression with reference system"
            ))

    def _detect_enum_patterns(self, data: Any, path: str) -> None:
        """Detect enum-like patterns (limited set of repeated values)."""
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, list) and len(value) > 5:
                    # Check if values repeat (enum-like)
                    unique_values = set(str(v) for v in value if not isinstance(v, (dict, list)))
                    if len(unique_values) < len(value) * 0.3:  # Less than 30% unique
                        confidence = 1.0 - (len(unique_values) / len(value))

                        self.detected_patterns.append(Pattern(
                            pattern_type=PatternType.ENUM_VALUES,
                            confidence=confidence,
                            location=f"{path}.{key}",
                            count=len(value),
                            compression_potential=0.6,
                            recommendation=f"Array with {len(unique_values)} unique values out of {len(value)} - use value dictionary"
                        ))

    def _detect_sparse_patterns(self, data: Any, path: str) -> None:
        """Detect sparse arrays/objects (many null values)."""
        if isinstance(data, dict):
            total_values = len(data)
            null_count = sum(1 for v in data.values() if v is None)

            if total_values > 5 and null_count / total_values > 0.5:
                sparsity = null_count / total_values

                self.detected_patterns.append(Pattern(
                    pattern_type=PatternType.SPARSE_ARRAY,
                    confidence=sparsity,
                    location=path,
                    compression_potential=0.4 + (sparsity * 0.3),
                    recommendation=f"Sparse object ({sparsity:.0%} null) - omit null values or use sparse representation"
                ))

        elif isinstance(data, list) and len(data) > 10:
            null_count = sum(1 for v in data if v is None)
            if null_count / len(data) > 0.5:
                sparsity = null_count / len(data)

                self.detected_patterns.append(Pattern(
                    pattern_type=PatternType.SPARSE_ARRAY,
                    confidence=sparsity,
                    location=path,
                    count=len(data),
                    compression_potential=0.5,
                    recommendation=f"Sparse array ({sparsity:.0%} null) - use run-length encoding"
                ))

    def _detect_deep_nesting(self, data: Any, path: str) -> None:
        """Detect deeply nested structures."""
        if self.nesting_depths:
            max_depth = max(self.nesting_depths)
            avg_depth = sum(self.nesting_depths) / len(self.nesting_depths)

            if max_depth > 5 or avg_depth > 3:
                confidence = min(max_depth / 10, 1.0)

                self.detected_patterns.append(Pattern(
                    pattern_type=PatternType.DEEP_NESTING,
                    confidence=confidence,
                    location=path,
                    compression_potential=0.4,
                    recommendation=f"Deep nesting (max: {max_depth}, avg: {avg_depth:.1f}) - flatten or use references"
                ))

    def _is_homogeneous_array(self, arr: List) -> bool:
        """Check if array contains all same type."""
        if not arr:
            return True
        first_type = type(arr[0])
        return all(isinstance(item, first_type) for item in arr)

    def _calculate_schema_consistency(self, arr: List[Dict]) -> float:
        """Calculate schema consistency score (0-1)."""
        if not arr:
            return 0.0

        key_sets = [set(item.keys()) for item in arr if isinstance(item, dict)]
        if not key_sets:
            return 0.0

        # Perfect match bonus
        if len(set(tuple(sorted(keys)) for keys in key_sets)) == 1:
            return 1.0

        # Calculate based on common vs total keys
        all_keys = set.union(*key_sets)
        common_keys = set.intersection(*key_sets)

        return len(common_keys) / len(all_keys) if all_keys else 0.0

    def get_compression_strategy(self, data: Any) -> CompressionStrategy:
        """
        Generate optimal compression strategy.

        Args:
            data: Data to analyze

        Returns:
            CompressionStrategy with detailed recommendations
        """
        patterns = self.analyze(data)

        strategy = CompressionStrategy(
            use_schema_compression=False,
            use_reference_compression=False,
            use_string_dictionary=False,
            use_value_compression=False,
            use_partial_schema=False,
            custom_abbreviations={},
            expected_savings=0.0,
            recommended_level=2,  # STANDARD by default
            patterns=patterns,
            reasoning=[]
        )

        # Analyze patterns to build strategy
        for pattern in patterns:
            if pattern.pattern_type == PatternType.CONSISTENT_SCHEMA_ARRAY:
                if pattern.confidence > 0.8:
                    strategy.use_schema_compression = True
                    strategy.expected_savings += 0.25
                    strategy.reasoning.append(
                        f"Schema compression recommended for {pattern.count} items with {pattern.confidence:.0%} consistency"
                    )
                elif pattern.confidence > 0.5:
                    strategy.use_partial_schema = True
                    strategy.expected_savings += 0.15
                    strategy.reasoning.append(
                        f"Partial schema compression for {pattern.confidence:.0%} consistent array"
                    )

            elif pattern.pattern_type == PatternType.REPEATED_STRUCTURE:
                if pattern.count >= 3:
                    strategy.use_reference_compression = True
                    strategy.expected_savings += min(0.20, pattern.count * 0.02)
                    strategy.reasoning.append(
                        f"Reference compression for structure repeated {pattern.count} times"
                    )

            elif pattern.pattern_type == PatternType.ENUM_VALUES:
                strategy.use_string_dictionary = True
                strategy.expected_savings += 0.15
                strategy.reasoning.append("String dictionary for repeated enum values")

            elif pattern.pattern_type in [PatternType.TIME_SERIES, PatternType.DATABASE_RECORD]:
                strategy.use_value_compression = True
                strategy.expected_savings += 0.10
                strategy.reasoning.append(f"Value compression for {pattern.pattern_type.value}")

        # Suggest custom abbreviations for frequent keys
        custom_abbrevs = self.suggest_custom_abbreviations()
        if custom_abbrevs:
            strategy.custom_abbreviations = custom_abbrevs
            strategy.expected_savings += len(custom_abbrevs) * 0.01

        # Determine recommended compression level
        if strategy.expected_savings > 0.6:
            strategy.recommended_level = 4  # EXTREME
            strategy.reasoning.append("EXTREME level recommended for maximum compression")
        elif strategy.expected_savings > 0.4:
            strategy.recommended_level = 3  # AGGRESSIVE
            strategy.reasoning.append("AGGRESSIVE level recommended for high compression")
        elif strategy.expected_savings > 0.2:
            strategy.recommended_level = 2  # STANDARD
            strategy.reasoning.append("STANDARD level provides good balance")
        else:
            strategy.recommended_level = 1  # MINIMAL
            strategy.reasoning.append("MINIMAL level sufficient for this data")

        # Cap expected savings
        strategy.expected_savings = min(strategy.expected_savings, 0.85)

        return strategy

    def suggest_custom_abbreviations(self) -> Dict[str, str]:
        """
        Generate custom abbreviations for frequent keys.

        Returns:
            Dictionary mapping keys to suggested abbreviations
        """
        suggestions = {}

        for key, count in self.key_frequency.most_common(20):
            if count < 3 or len(key) <= 3:
                continue

            # Generate smart abbreviation
            abbrev = self._generate_abbreviation(key)
            if abbrev and abbrev != key:
                suggestions[key] = abbrev

        return suggestions

    def _generate_abbreviation(self, key: str) -> str:
        """Generate smart abbreviation for a key."""
        # Remove common suffixes
        key_clean = re.sub(r'_(id|name|code|type|status|at)$', '', key)

        # Camel case to initials
        if re.match(r'^[a-z]+[A-Z]', key):
            parts = re.findall(r'[A-Z][a-z]*', key)
            if parts:
                return ''.join(p[0].lower() for p in parts)

        # Snake case abbreviation
        if '_' in key_clean:
            parts = key_clean.split('_')
            if len(parts) <= 3:
                return ''.join(p[0] for p in parts)

        # Remove vowels (keep first letter)
        abbrev = key_clean[0] + ''.join(c for c in key_clean[1:] if c not in 'aeiouAEIOU')

        # Limit length
        return abbrev[:4].lower()

    def get_recommendations(self) -> List[str]:
        """
        Get human-readable compression recommendations.

        Returns:
            List of recommendation strings
        """
        recommendations = []

        for pattern in self.detected_patterns[:10]:  # Top 10 patterns
            if pattern.compression_potential > 0.5:
                recommendations.append(
                    f"🎯 {pattern.recommendation} "
                    f"(confidence: {pattern.confidence:.0%}, "
                    f"potential: {pattern.compression_potential:.0%})"
                )

        # Add general recommendations based on statistics
        if self.key_frequency:
            top_keys = self.key_frequency.most_common(5)
            recommendations.append(
                f"📊 Top frequent keys: {', '.join(k for k, _ in top_keys)}"
            )

        if self.array_sizes:
            avg_size = sum(self.array_sizes) / len(self.array_sizes)
            max_size = max(self.array_sizes)
            recommendations.append(
                f"📈 Array statistics: avg={avg_size:.0f}, max={max_size}"
            )

        return recommendations
