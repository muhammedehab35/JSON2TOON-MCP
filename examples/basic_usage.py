"""
JSON2TOON - Basic Usage Examples
Demonstrates core functionality with practical examples.
"""

import json
from src.advanced_converter import (
    AdvancedTOONConverter,
    convert_json_to_toon,
    convert_toon_to_json,
    CompressionLevel
)
from src.pattern_analyzer import AdvancedPatternAnalyzer
from src.optimizer import SmartOptimizer


def example_1_basic_conversion():
    """Example 1: Basic JSON to TOON conversion."""
    print("=" * 60)
    print("Example 1: Basic Conversion")
    print("=" * 60)

    data = {
        "id": 12345,
        "name": "John Doe",
        "email": "john@example.com",
        "type": "user",
        "status": "active",
        "created_at": "2025-01-01T00:00:00Z"
    }

    # Convert to TOON (STANDARD level)
    toon = convert_json_to_toon(data, level=CompressionLevel.STANDARD)

    print(f"\nOriginal JSON ({len(json.dumps(data))} bytes):")
    print(json.dumps(data, indent=2))

    print(f"\nTOON Format ({len(toon)} bytes):")
    print(toon)

    # Convert back
    restored = convert_toon_to_json(toon)
    print(f"\nRestored JSON:")
    print(restored)

    savings = (1 - len(toon) / len(json.dumps(data))) * 100
    print(f"\n✅ Savings: {savings:.1f}%")


def example_2_compression_levels():
    """Example 2: Compare different compression levels."""
    print("\n" + "=" * 60)
    print("Example 2: Compression Level Comparison")
    print("=" * 60)

    data = {
        "users": [
            {
                "id": i,
                "name": f"User {i}",
                "email": f"user{i}@example.com",
                "status": "active"
            }
            for i in range(20)
        ]
    }

    original_size = len(json.dumps(data))
    print(f"\nOriginal size: {original_size} bytes\n")

    levels = [
        (CompressionLevel.MINIMAL, "MINIMAL"),
        (CompressionLevel.STANDARD, "STANDARD"),
        (CompressionLevel.AGGRESSIVE, "AGGRESSIVE"),
        (CompressionLevel.EXTREME, "EXTREME")
    ]

    for level, name in levels:
        converter = AdvancedTOONConverter(level=level)
        toon = converter.json_to_toon(data)
        metrics = converter.calculate_metrics(json.dumps(data), toon)

        print(f"{name:12} - Size: {metrics.compressed_size:5} bytes - "
              f"Savings: {metrics.savings_percent:5.1f}% - "
              f"Ratio: {metrics.compression_ratio:.3f}")


def example_3_pattern_analysis():
    """Example 3: Advanced pattern analysis."""
    print("\n" + "=" * 60)
    print("Example 3: Pattern Analysis")
    print("=" * 60)

    data = {
        "status": "success",
        "data": {
            "users": [
                {
                    "id": i,
                    "username": f"user{i}",
                    "email": f"user{i}@example.com",
                    "profile": {
                        "first_name": f"First{i}",
                        "last_name": f"Last{i}"
                    },
                    "created_at": "2025-01-01T00:00:00Z",
                    "updated_at": "2025-01-15T10:30:00Z"
                }
                for i in range(15)
            ]
        },
        "pagination": {
            "page": 1,
            "per_page": 15,
            "total": 100
        }
    }

    analyzer = AdvancedPatternAnalyzer()
    patterns = analyzer.analyze(data)

    print(f"\n🔍 Detected {len(patterns)} patterns:\n")
    for pattern in patterns[:5]:  # Show top 5
        print(f"  • {pattern.pattern_type.value}")
        print(f"    Confidence: {pattern.confidence:.1%}")
        print(f"    Compression potential: {pattern.compression_potential:.1%}")
        print(f"    Recommendation: {pattern.recommendation}\n")


def example_4_smart_optimization():
    """Example 4: Smart automatic optimization."""
    print("\n" + "=" * 60)
    print("Example 4: Smart Optimization")
    print("=" * 60)

    data = {
        "products": [
            {
                "id": i,
                "name": f"Product {i}",
                "price": 99.99 + i,
                "category": "Electronics" if i % 2 == 0 else "Books",
                "in_stock": True,
                "created_at": "2025-01-01T00:00:00Z"
            }
            for i in range(30)
        ]
    }

    optimizer = SmartOptimizer()

    print("\nTesting different profiles:\n")

    for profile in ["speed", "balanced", "size"]:
        result = optimizer.optimize(data, profile=profile)

        print(f"Profile: {profile.upper()}")
        print(f"  Level selected: {result['level_selected']}")
        print(f"  Savings: {result['metrics']['savings_percent']:.1f}%")
        print(f"  Compressed size: {result['metrics']['compressed_size']} bytes")
        print()


def example_5_batch_processing():
    """Example 5: High-performance batch processing."""
    print("\n" + "=" * 60)
    print("Example 5: Batch Processing")
    print("=" * 60)

    # Generate 100 items
    items = [
        {
            "id": i,
            "timestamp": "2025-01-01T00:00:00Z",
            "value": i * 10,
            "status": "processed"
        }
        for i in range(100)
    ]

    converter = AdvancedTOONConverter(level=CompressionLevel.AGGRESSIVE)

    total_original = 0
    total_compressed = 0

    print(f"\nProcessing {len(items)} items...")

    for item in items:
        original_json = json.dumps(item)
        toon = converter.json_to_toon(item)

        total_original += len(original_json)
        total_compressed += len(toon)

    print(f"\nResults:")
    print(f"  Total original: {total_original:,} bytes")
    print(f"  Total compressed: {total_compressed:,} bytes")
    print(f"  Total saved: {total_original - total_compressed:,} bytes")
    print(f"  Savings: {(1 - total_compressed / total_original) * 100:.1f}%")


def example_6_compression_strategy():
    """Example 6: Get optimal compression strategy."""
    print("\n" + "=" * 60)
    print("Example 6: Compression Strategy Recommendation")
    print("=" * 60)

    data = {
        "orders": [
            {
                "order_id": f"ORD-{i:05d}",
                "customer_id": i % 50,
                "items": [
                    {"product_id": j, "quantity": 1}
                    for j in range(3)
                ],
                "total": 299.99,
                "status": "shipped",
                "created_at": "2025-01-01T00:00:00Z"
            }
            for i in range(25)
        ]
    }

    analyzer = AdvancedPatternAnalyzer()
    strategy = analyzer.get_compression_strategy(data)

    print(f"\n📊 Compression Strategy Analysis:\n")
    print(f"Recommended level: {strategy.recommended_level} "
          f"({['MINIMAL', 'STANDARD', 'AGGRESSIVE', 'EXTREME'][strategy.recommended_level - 1]})")
    print(f"Expected savings: {strategy.expected_savings * 100:.1f}%")

    print(f"\n🎯 Optimizations to apply:")
    print(f"  Schema compression: {'✅' if strategy.use_schema_compression else '❌'}")
    print(f"  Reference compression: {'✅' if strategy.use_reference_compression else '❌'}")
    print(f"  String dictionary: {'✅' if strategy.use_string_dictionary else '❌'}")
    print(f"  Value compression: {'✅' if strategy.use_value_compression else '❌'}")

    if strategy.reasoning:
        print(f"\n💡 Reasoning:")
        for reason in strategy.reasoning[:3]:
            print(f"  • {reason}")


def example_7_custom_abbreviations():
    """Example 7: Generate custom abbreviations."""
    print("\n" + "=" * 60)
    print("Example 7: Custom Abbreviation Suggestions")
    print("=" * 60)

    data = {
        "product_id": 1,
        "product_name": "Widget",
        "product_category": "Hardware",
        "product_price": 29.99,
        "product_stock": 100,
        "product_description": "A great widget"
    }

    analyzer = AdvancedPatternAnalyzer()
    analyzer.analyze(data)
    suggestions = analyzer.suggest_custom_abbreviations()

    print("\n🔤 Custom abbreviation suggestions:\n")
    for original, abbreviated in suggestions.items():
        print(f"  {original:25} → {abbreviated}")


def example_8_metrics_and_validation():
    """Example 8: Detailed metrics and validation."""
    print("\n" + "=" * 60)
    print("Example 8: Metrics and Validation")
    print("=" * 60)

    data = {
        "api_version": "2.0",
        "timestamp": "2025-01-15T10:30:00Z",
        "data": [
            {"id": i, "value": i * 100}
            for i in range(50)
        ]
    }

    converter = AdvancedTOONConverter(level=CompressionLevel.AGGRESSIVE)
    original_json = json.dumps(data)
    toon = converter.json_to_toon(data)
    metrics = converter.calculate_metrics(original_json, toon)

    print(f"\n📈 Detailed Metrics:\n")
    print(f"Original size: {metrics.original_size:,} bytes")
    print(f"Compressed size: {metrics.compressed_size:,} bytes")
    print(f"Bytes saved: {metrics.original_size - metrics.compressed_size:,}")
    print(f"Savings percent: {metrics.savings_percent:.2f}%")
    print(f"Compression ratio: {metrics.compression_ratio:.3f}")
    print(f"Compression level: {metrics.compression_level.name}")

    print(f"\n🔧 Techniques applied:")
    print(f"  Abbreviations used: {metrics.abbreviations_used}")
    print(f"  Schema compressions: {metrics.schema_compressions}")
    print(f"  Value compressions: {metrics.value_compressions}")
    print(f"  References: {metrics.reference_count}")

    # Validate round-trip
    restored = convert_toon_to_json(toon)
    is_valid = json.loads(restored) == data
    print(f"\n✅ Round-trip validation: {'PASSED' if is_valid else 'FAILED'}")


def main():
    """Run all examples."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 12 + "JSON2TOON v2.0 - Usage Examples" + " " * 14 + "║")
    print("╚" + "=" * 58 + "╝")

    examples = [
        example_1_basic_conversion,
        example_2_compression_levels,
        example_3_pattern_analysis,
        example_4_smart_optimization,
        example_5_batch_processing,
        example_6_compression_strategy,
        example_7_custom_abbreviations,
        example_8_metrics_and_validation
    ]

    for example_func in examples:
        try:
            example_func()
        except Exception as e:
            print(f"\n❌ Error in {example_func.__name__}: {e}")

    print("\n" + "=" * 60)
    print("✅ All examples completed!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
