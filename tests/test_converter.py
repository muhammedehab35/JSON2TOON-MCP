"""
Tests for Advanced TOON Converter
"""

import json
import pytest
from src.advanced_converter import (
    AdvancedTOONConverter,
    convert_json_to_toon,
    convert_toon_to_json,
    CompressionLevel
)


class TestAdvancedConverter:
    """Test suite for AdvancedTOONConverter."""

    def test_simple_conversion_minimal(self):
        """Test simple object conversion with MINIMAL level."""
        data = {
            "id": 123,
            "name": "Test User",
            "type": "user",
            "status": "active"
        }

        converter = AdvancedTOONConverter(level=CompressionLevel.MINIMAL)
        toon = converter.json_to_toon(data)

        toon_obj = json.loads(toon)
        assert '_toon' in toon_obj
        assert toon_obj['_toon'] == '2.0'
        assert toon_obj['_lvl'] == 1

        # Should have abbreviated keys
        assert 'i' in toon_obj['d']  # id -> i
        assert 'n' in toon_obj['d']  # name -> n
        assert 't' in toon_obj['d']  # type -> t
        assert 's' in toon_obj['d']  # status -> s

    def test_round_trip_all_levels(self):
        """Test round-trip conversion for all compression levels."""
        original_data = {
            "id": 456,
            "name": "Test Item",
            "type": "product",
            "status": "active",
            "price": 99.99,
            "tags": ["electronics", "gadgets"],
            "metadata": {
                "created_at": "2025-01-01T00:00:00Z",
                "updated_at": "2025-01-15T10:30:00Z",
                "views": 1500
            }
        }

        for level in [1, 2, 3, 4]:
            converter = AdvancedTOONConverter(level=CompressionLevel(level))
            toon = converter.json_to_toon(original_data)
            json_str = converter.toon_to_json(toon)
            restored_data = json.loads(json_str)

            assert restored_data == original_data, f"Round-trip failed for level {level}"

    def test_null_and_boolean_conversion(self):
        """Test null and boolean value conversion."""
        data = {
            "value": None,
            "enabled": True,
            "disabled": False,
            "optional": None
        }

        converter = AdvancedTOONConverter(level=CompressionLevel.STANDARD)
        toon = converter.json_to_toon(data)
        toon_obj = json.loads(toon)

        # Null should be ~
        assert toon_obj['d']['v'] == '~'
        assert toon_obj['d']['optional'] == '~'

        # Booleans should be T/F
        assert toon_obj['d']['en'] == 'T'
        assert toon_obj['d']['dis'] == 'F'

        # Round-trip
        json_str = converter.toon_to_json(toon)
        restored = json.loads(json_str)
        assert restored == data

    def test_schema_compression(self):
        """Test schema-based array compression."""
        data = [
            {"id": 1, "name": "Item 1", "type": "A", "price": 10.0},
            {"id": 2, "name": "Item 2", "type": "B", "price": 20.0},
            {"id": 3, "name": "Item 3", "type": "C", "price": 30.0}
        ]

        converter = AdvancedTOONConverter(level=CompressionLevel.STANDARD)
        toon = converter.json_to_toon(data)
        toon_obj = json.loads(toon)

        # Should use schema compression
        data_content = toon_obj['d']
        assert '_sch' in data_content
        assert '_dat' in data_content

        # Verify schema
        assert 'i' in data_content['_sch']  # id
        assert 'n' in data_content['_sch']  # name
        assert 't' in data_content['_sch']  # type

        # Round-trip
        json_str = converter.toon_to_json(toon)
        restored = json.loads(json_str)
        assert restored == data

    def test_large_array_compression(self):
        """Test compression of large arrays."""
        data = [
            {
                "id": i,
                "name": f"User {i}",
                "email": f"user{i}@example.com",
                "status": "active" if i % 2 == 0 else "inactive",
                "created_at": "2025-01-01T00:00:00Z"
            }
            for i in range(200)
        ]

        converter = AdvancedTOONConverter(level=CompressionLevel.AGGRESSIVE)
        original_json = json.dumps(data)
        toon = converter.json_to_toon(data)

        # Calculate savings
        metrics = converter.calculate_metrics(original_json, toon)
        assert metrics.savings_percent > 50  # Should save at least 50%

        # Round-trip verification
        json_str = converter.toon_to_json(toon)
        restored = json.loads(json_str)
        assert restored == data

    def test_nested_objects(self):
        """Test deeply nested object conversion."""
        data = {
            "user": {
                "id": 1,
                "profile": {
                    "name": "John Doe",
                    "contact": {
                        "email": "john@example.com",
                        "phone": "+1234567890",
                        "address": {
                            "street": "123 Main St",
                            "city": "New York",
                            "country": "USA"
                        }
                    }
                }
            }
        }

        converter = AdvancedTOONConverter(level=CompressionLevel.AGGRESSIVE)
        toon = converter.json_to_toon(data)

        # Round-trip
        json_str = converter.toon_to_json(toon)
        restored = json.loads(json_str)
        assert restored == data

    def test_extreme_compression_with_zlib(self):
        """Test EXTREME level with zlib compression."""
        data = {
            "items": [
                {"id": i, "data": f"Some data {i}" * 10}
                for i in range(100)
            ]
        }

        converter = AdvancedTOONConverter(level=CompressionLevel.EXTREME)
        original_json = json.dumps(data)
        toon = converter.json_to_toon(data)

        # Should use zlib
        toon_obj = json.loads(toon)
        assert toon_obj.get('_zlib') == True

        # Should have significant compression
        assert len(toon) < len(original_json) * 0.4  # Less than 40% of original

        # Round-trip
        json_str = converter.toon_to_json(toon)
        restored = json.loads(json_str)
        assert restored == data

    def test_metrics_calculation(self):
        """Test detailed metrics calculation."""
        data = {
            "users": [
                {"id": i, "name": f"User {i}", "email": f"user{i}@test.com"}
                for i in range(50)
            ]
        }

        converter = AdvancedTOONConverter(level=CompressionLevel.STANDARD)
        original_json = json.dumps(data)
        toon = converter.json_to_toon(data)
        metrics = converter.calculate_metrics(original_json, toon)

        assert metrics.original_size > 0
        assert metrics.compressed_size > 0
        assert metrics.compressed_size < metrics.original_size
        assert metrics.savings_percent > 0
        assert metrics.compression_ratio < 1.0
        assert metrics.compression_level == CompressionLevel.STANDARD
        assert metrics.abbreviations_used > 0

    def test_convenience_functions(self):
        """Test convenience functions."""
        data = {"id": 1, "name": "Test", "status": "active"}

        # Test convert_json_to_toon
        toon = convert_json_to_toon(data, level=CompressionLevel.STANDARD)
        assert isinstance(toon, str)

        # Test convert_toon_to_json
        json_str = convert_toon_to_json(toon)
        restored = json.loads(json_str)
        assert restored == data

    def test_mixed_data_types(self):
        """Test conversion with mixed data types."""
        data = {
            "string": "test",
            "integer": 42,
            "float": 3.14,
            "boolean": True,
            "null": None,
            "array": [1, 2, 3],
            "object": {"nested": "value"},
            "mixed_array": [1, "two", 3.0, None, True]
        }

        converter = AdvancedTOONConverter(level=CompressionLevel.STANDARD)
        toon = converter.json_to_toon(data)

        # Round-trip
        json_str = converter.toon_to_json(toon)
        restored = json.loads(json_str)
        assert restored == data

    def test_empty_structures(self):
        """Test handling of empty structures."""
        test_cases = [
            {},
            [],
            {"empty_dict": {}, "empty_list": []},
            [[], {}, None]
        ]

        converter = AdvancedTOONConverter(level=CompressionLevel.STANDARD)

        for data in test_cases:
            toon = converter.json_to_toon(data)
            json_str = converter.toon_to_json(toon)
            restored = json.loads(json_str)
            assert restored == data

    def test_unicode_handling(self):
        """Test Unicode character handling."""
        data = {
            "chinese": "你好世界",
            "arabic": "مرحبا بالعالم",
            "emoji": "🎉🎊🎈",
            "mixed": "Hello 世界 🌍"
        }

        converter = AdvancedTOONConverter(level=CompressionLevel.STANDARD)
        toon = converter.json_to_toon(data)

        # Round-trip
        json_str = converter.toon_to_json(toon)
        restored = json.loads(json_str)
        assert restored == data

    def test_value_pattern_compression(self):
        """Test compression of value patterns (timestamps, UUIDs)."""
        data = {
            "timestamp": "2025-01-01T00:00:00Z",
            "uuid": "550e8400-e29b-41d4-a716-446655440000",
            "email": "test@example.com"
        }

        converter = AdvancedTOONConverter(level=CompressionLevel.AGGRESSIVE)
        toon = converter.json_to_toon(data)

        # Should detect patterns
        assert converter.metrics['value_compressions'] > 0

        # Round-trip
        json_str = converter.toon_to_json(toon)
        restored = json.loads(json_str)
        assert restored == data


class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_invalid_toon_format(self):
        """Test handling of invalid TOON format."""
        converter = AdvancedTOONConverter()

        with pytest.raises(ValueError):
            converter.toon_to_json('{"invalid": "format"}')

    def test_very_large_numbers(self):
        """Test handling of very large numbers."""
        data = {
            "large_int": 9999999999999999,
            "large_float": 9.999999999999999e100,
            "small_float": 1.234567890123456e-100
        }

        converter = AdvancedTOONConverter(level=CompressionLevel.STANDARD)
        toon = converter.json_to_toon(data)

        json_str = converter.toon_to_json(toon)
        restored = json.loads(json_str)
        assert restored == data

    def test_special_characters_in_keys(self):
        """Test keys with special characters."""
        data = {
            "key-with-dash": "value1",
            "key_with_underscore": "value2",
            "key.with.dots": "value3",
            "key$with$dollar": "value4"
        }

        converter = AdvancedTOONConverter(level=CompressionLevel.STANDARD)
        toon = converter.json_to_toon(data)

        json_str = converter.toon_to_json(toon)
        restored = json.loads(json_str)
        assert restored == data


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--cov=src.advanced_converter"])
