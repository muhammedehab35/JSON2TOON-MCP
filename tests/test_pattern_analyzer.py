"""
Tests for Advanced Pattern Analyzer
"""

import json
import pytest
from src.pattern_analyzer import (
    AdvancedPatternAnalyzer,
    PatternType,
    CompressionStrategy
)


class TestPatternAnalyzer:
    """Test suite for AdvancedPatternAnalyzer."""

    def test_api_response_detection(self):
        """Test detection of API response patterns."""
        data = {
            "status": "success",
            "data": {"id": 1, "name": "Test"},
            "message": "OK",
            "meta": {"page": 1, "total": 100}
        }

        analyzer = AdvancedPatternAnalyzer()
        patterns = analyzer.analyze(data)

        api_patterns = [p for p in patterns if p.pattern_type == PatternType.API_RESPONSE]
        assert len(api_patterns) > 0
        assert api_patterns[0].confidence > 0.4

    def test_database_record_detection(self):
        """Test detection of database record patterns."""
        data = {
            "id": 1,
            "name": "Test Record",
            "created_at": "2025-01-01T00:00:00Z",
            "updated_at": "2025-01-15T10:30:00Z"
        }

        analyzer = AdvancedPatternAnalyzer()
        patterns = analyzer.analyze(data)

        db_patterns = [p for p in patterns if p.pattern_type == PatternType.DATABASE_RECORD]
        assert len(db_patterns) > 0

    def test_database_records_array(self):
        """Test detection of database records array."""
        data = [
            {"id": i, "created_at": "2025-01-01T00:00:00Z", "updated_at": "2025-01-01T00:00:00Z"}
            for i in range(20)
        ]

        analyzer = AdvancedPatternAnalyzer()
        patterns = analyzer.analyze(data)

        db_patterns = [p for p in patterns if p.pattern_type == PatternType.DATABASE_RECORD]
        assert len(db_patterns) > 0
        assert any(p.count == 20 for p in db_patterns)

    def test_user_data_detection(self):
        """Test detection of user data patterns."""
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "hashed_password",
            "first_name": "John",
            "last_name": "Doe"
        }

        analyzer = AdvancedPatternAnalyzer()
        patterns = analyzer.analyze(data)

        user_patterns = [p for p in patterns if p.pattern_type == PatternType.USER_DATA]
        assert len(user_patterns) > 0

    def test_nested_patterns_detection(self):
        """Test detection of nested structure patterns."""
        data = {
            "user": {
                "address": {
                    "street": "123 Main St",
                    "city": "New York",
                    "state": "NY",
                    "postal_code": "10001",
                    "country": "USA"
                },
                "coordinates": {
                    "latitude": 40.7128,
                    "longitude": -74.0060
                }
            }
        }

        analyzer = AdvancedPatternAnalyzer()
        patterns = analyzer.analyze(data)

        nested_patterns = [
            p for p in patterns
            if 'NESTED' in p.pattern_type.name
        ]
        assert len(nested_patterns) > 0

    def test_pagination_pattern(self):
        """Test detection of pagination patterns."""
        data = {
            "items": [1, 2, 3],
            "page": 1,
            "per_page": 20,
            "total_pages": 5,
            "total_count": 100
        }

        analyzer = AdvancedPatternAnalyzer()
        patterns = analyzer.analyze(data)

        pagination_patterns = [p for p in patterns if p.pattern_type == PatternType.PAGINATION]
        assert len(pagination_patterns) > 0

    def test_homogeneous_array_detection(self):
        """Test detection of homogeneous arrays."""
        data = {
            "numbers": [1, 2, 3, 4, 5],
            "strings": ["a", "b", "c", "d"],
            "booleans": [True, False, True, False]
        }

        analyzer = AdvancedPatternAnalyzer()
        patterns = analyzer.analyze(data)

        homogeneous_patterns = [
            p for p in patterns
            if p.pattern_type == PatternType.HOMOGENEOUS_ARRAY
        ]
        assert len(homogeneous_patterns) >= 3  # One for each array

    def test_consistent_schema_array(self):
        """Test detection of consistent schema arrays."""
        data = {
            "users": [
                {"id": 1, "name": "User 1", "email": "user1@test.com"},
                {"id": 2, "name": "User 2", "email": "user2@test.com"},
                {"id": 3, "name": "User 3", "email": "user3@test.com"}
            ]
        }

        analyzer = AdvancedPatternAnalyzer()
        patterns = analyzer.analyze(data)

        schema_patterns = [
            p for p in patterns
            if p.pattern_type == PatternType.CONSISTENT_SCHEMA_ARRAY
        ]
        assert len(schema_patterns) > 0
        assert schema_patterns[0].confidence > 0.9  # Perfect schema match

    def test_repeated_structure_detection(self):
        """Test detection of repeated structures."""
        data = {
            "items": [
                {"type": "A", "value": 1, "status": "active"},
                {"type": "B", "value": 2, "status": "inactive"},
                {"type": "C", "value": 3, "status": "active"},
                {"type": "D", "value": 4, "status": "active"}
            ]
        }

        analyzer = AdvancedPatternAnalyzer()
        patterns = analyzer.analyze(data)

        repeated_patterns = [
            p for p in patterns
            if p.pattern_type == PatternType.REPEATED_STRUCTURE
        ]
        assert len(repeated_patterns) > 0

    def test_time_series_detection(self):
        """Test detection of time series patterns."""
        data = [
            {"timestamp": "2025-01-01T00:00:00Z", "value": 100},
            {"timestamp": "2025-01-01T01:00:00Z", "value": 105},
            {"timestamp": "2025-01-01T02:00:00Z", "value": 110},
            {"timestamp": "2025-01-01T03:00:00Z", "value": 108},
            {"timestamp": "2025-01-01T04:00:00Z", "value": 112}
        ]

        analyzer = AdvancedPatternAnalyzer()
        patterns = analyzer.analyze(data)

        time_series_patterns = [
            p for p in patterns
            if p.pattern_type == PatternType.TIME_SERIES
        ]
        assert len(time_series_patterns) > 0

    def test_graph_pattern_detection(self):
        """Test detection of graph/node patterns."""
        data = {
            "id": "node1",
            "neighbors": ["node2", "node3"],
            "edges": [
                {"from": "node1", "to": "node2"},
                {"from": "node1", "to": "node3"}
            ]
        }

        analyzer = AdvancedPatternAnalyzer()
        patterns = analyzer.analyze(data)

        graph_patterns = [
            p for p in patterns
            if p.pattern_type == PatternType.GRAPH_NODE
        ]
        assert len(graph_patterns) > 0

    def test_tree_structure_detection(self):
        """Test detection of tree structures."""
        data = {
            "id": 1,
            "value": "root",
            "children": [
                {
                    "id": 2,
                    "value": "child1",
                    "children": []
                },
                {
                    "id": 3,
                    "value": "child2",
                    "children": []
                }
            ]
        }

        analyzer = AdvancedPatternAnalyzer()
        patterns = analyzer.analyze(data)

        tree_patterns = [
            p for p in patterns
            if p.pattern_type == PatternType.TREE_STRUCTURE
        ]
        assert len(tree_patterns) > 0

    def test_enum_pattern_detection(self):
        """Test detection of enum-like patterns."""
        data = {
            "statuses": ["active"] * 10 + ["inactive"] * 8 + ["pending"] * 5
        }

        analyzer = AdvancedPatternAnalyzer()
        patterns = analyzer.analyze(data)

        enum_patterns = [
            p for p in patterns
            if p.pattern_type == PatternType.ENUM_VALUES
        ]
        assert len(enum_patterns) > 0

    def test_sparse_array_detection(self):
        """Test detection of sparse arrays."""
        data = {
            "values": [None] * 20 + [1, 2, 3] + [None] * 30
        }

        analyzer = AdvancedPatternAnalyzer()
        patterns = analyzer.analyze(data)

        sparse_patterns = [
            p for p in patterns
            if p.pattern_type == PatternType.SPARSE_ARRAY
        ]
        assert len(sparse_patterns) > 0

    def test_deep_nesting_detection(self):
        """Test detection of deep nesting."""
        data = {
            "level1": {
                "level2": {
                    "level3": {
                        "level4": {
                            "level5": {
                                "level6": {
                                    "value": "deep"
                                }
                            }
                        }
                    }
                }
            }
        }

        analyzer = AdvancedPatternAnalyzer()
        patterns = analyzer.analyze(data)

        deep_patterns = [
            p for p in patterns
            if p.pattern_type == PatternType.DEEP_NESTING
        ]
        assert len(deep_patterns) > 0

    def test_compression_strategy_generation(self):
        """Test compression strategy generation."""
        data = {
            "users": [
                {
                    "id": i,
                    "name": f"User {i}",
                    "email": f"user{i}@example.com",
                    "created_at": "2025-01-01T00:00:00Z"
                }
                for i in range(50)
            ]
        }

        analyzer = AdvancedPatternAnalyzer()
        strategy = analyzer.get_compression_strategy(data)

        assert isinstance(strategy, CompressionStrategy)
        assert strategy.expected_savings > 0
        assert strategy.recommended_level in [1, 2, 3, 4]
        assert len(strategy.reasoning) > 0

        # Should recommend schema compression for consistent array
        assert strategy.use_schema_compression == True

    def test_custom_abbreviation_suggestions(self):
        """Test custom abbreviation suggestions."""
        data = {
            "product_id": 1,
            "product_name": "Test",
            "product_category": "Electronics",
            "product_price": 99.99,
            "product_stock": 50
        }

        analyzer = AdvancedPatternAnalyzer()
        analyzer.analyze(data)
        suggestions = analyzer.suggest_custom_abbreviations()

        assert len(suggestions) > 0
        # Should suggest abbreviations for frequent "product_" prefix

    def test_recommendations_generation(self):
        """Test generation of human-readable recommendations."""
        data = {
            "items": [
                {"id": i, "value": i * 10}
                for i in range(100)
            ]
        }

        analyzer = AdvancedPatternAnalyzer()
        analyzer.analyze(data)
        recommendations = analyzer.get_recommendations()

        assert len(recommendations) > 0
        assert all(isinstance(r, str) for r in recommendations)

    def test_schema_consistency_calculation(self):
        """Test schema consistency calculation."""
        # Perfect consistency
        perfect_data = [
            {"a": 1, "b": 2, "c": 3},
            {"a": 4, "b": 5, "c": 6},
            {"a": 7, "b": 8, "c": 9}
        ]

        analyzer = AdvancedPatternAnalyzer()
        consistency = analyzer._calculate_schema_consistency(perfect_data)
        assert consistency == 1.0

        # Partial consistency
        partial_data = [
            {"a": 1, "b": 2, "c": 3},
            {"a": 4, "b": 5},
            {"a": 7, "b": 8, "c": 9}
        ]

        consistency = analyzer._calculate_schema_consistency(partial_data)
        assert 0.5 < consistency < 1.0

    def test_complex_real_world_data(self):
        """Test with complex real-world-like data."""
        data = {
            "api_version": "2.0",
            "status": "success",
            "data": {
                "users": [
                    {
                        "id": i,
                        "username": f"user{i}",
                        "email": f"user{i}@example.com",
                        "profile": {
                            "first_name": f"First{i}",
                            "last_name": f"Last{i}",
                            "avatar": f"https://example.com/avatar{i}.jpg",
                            "bio": f"Bio for user {i}"
                        },
                        "created_at": "2025-01-01T00:00:00Z",
                        "updated_at": "2025-01-15T10:30:00Z",
                        "status": "active" if i % 2 == 0 else "inactive"
                    }
                    for i in range(30)
                ],
                "pagination": {
                    "page": 1,
                    "per_page": 30,
                    "total_pages": 5,
                    "total_count": 150
                }
            },
            "meta": {
                "request_id": "req_12345",
                "timestamp": "2025-01-15T10:30:00Z",
                "took_ms": 45
            }
        }

        analyzer = AdvancedPatternAnalyzer()
        patterns = analyzer.analyze(data)
        strategy = analyzer.get_compression_strategy(data)

        # Should detect multiple pattern types
        assert len(patterns) >= 5

        # Should have high expected savings
        assert strategy.expected_savings > 0.4

        # Should recommend multiple optimizations
        assert len(strategy.reasoning) >= 3


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--cov=src.pattern_analyzer"])
