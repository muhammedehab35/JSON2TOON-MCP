# JSON2TOON Quick Start Guide 🚀

Get started with JSON2TOON in 5 minutes!

## Installation

```bash
# Navigate to project directory
cd JSON2TOON

# Install dependencies
pip install -r requirements.txt

# Install package
pip install -e .
```

## Test Installation

```bash
# Run a simple test
python -c "from src.advanced_converter import convert_json_to_toon; print('✅ Installation successful!')"
```

## Quick Examples

### 1. Basic Conversion

```python
from src.advanced_converter import convert_json_to_toon, convert_toon_to_json

# Your JSON data
data = {"id": 123, "name": "Test", "status": "active"}

# Compress
toon = convert_json_to_toon(data)
print(f"Compressed: {toon}")

# Decompress
original = convert_toon_to_json(toon)
print(f"Original: {original}")
```

### 2. Choose Compression Level

```python
from src.advanced_converter import convert_json_to_toon, CompressionLevel

# Level 1: MINIMAL (fastest)
toon_minimal = convert_json_to_toon(data, level=CompressionLevel.MINIMAL)

# Level 2: STANDARD (balanced) - Default
toon_standard = convert_json_to_toon(data, level=CompressionLevel.STANDARD)

# Level 3: AGGRESSIVE (high compression)
toon_aggressive = convert_json_to_toon(data, level=CompressionLevel.AGGRESSIVE)

# Level 4: EXTREME (maximum compression)
toon_extreme = convert_json_to_toon(data, level=CompressionLevel.EXTREME)
```

### 3. Auto-Optimize (Recommended)

```python
from src.optimizer import SmartOptimizer

optimizer = SmartOptimizer()

# Automatic best compression
result = optimizer.optimize(data, profile="balanced")
print(f"Savings: {result['metrics']['savings_percent']:.1f}%")
```

## Run Examples

```bash
# Run all examples
python examples/basic_usage.py
```

## Run Tests

```bash
# All tests
pytest tests/ -v

# Specific test
pytest tests/test_converter.py -v
```

## MCP Server Setup

### 1. Configure Claude Desktop

Edit `~/.config/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "json2toon": {
      "command": "python",
      "args": ["-m", "src.mcp_server"],
      "cwd": "/full/path/to/JSON2TOON"
    }
  }
}
```

### 2. Start Server

```bash
python -m src.mcp_server
```

### 3. Test in Claude

Try these commands in Claude:

```
Use the convert_to_toon tool to compress this JSON:
{"id": 1, "name": "Test", "email": "test@example.com"}

Use the analyze_patterns tool to analyze patterns in my data.

Use the smart_optimize tool with balanced profile.
```

## Docker Quick Start

### Build & Run

```bash
# Build image
docker build -t json2toon:2.0.0 .

# Run with Docker Compose
docker-compose up -d
```

### MCP with Docker

Update Claude config:

```json
{
  "mcpServers": {
    "json2toon": {
      "command": "docker",
      "args": ["run", "-i", "json2toon:2.0.0"]
    }
  }
}
```

## Common Use Cases

### Compress API Response

```python
api_response = {
    "status": "success",
    "data": [
        {"id": i, "name": f"Item {i}"}
        for i in range(100)
    ]
}

toon = convert_json_to_toon(api_response, level=CompressionLevel.AGGRESSIVE)
# Saves 60-70%!
```

### Analyze Before Compressing

```python
from src.pattern_analyzer import AdvancedPatternAnalyzer

analyzer = AdvancedPatternAnalyzer()

# Get recommendations
strategy = analyzer.get_compression_strategy(your_data)
print(f"Expected savings: {strategy.expected_savings * 100:.1f}%")
print(f"Recommended level: {strategy.recommended_level}")
```

### Batch Process Files

```python
import json
from pathlib import Path

converter = AdvancedTOONConverter(level=CompressionLevel.STANDARD)

for file in Path("data/").glob("*.json"):
    with open(file) as f:
        data = json.load(f)

    toon = converter.json_to_toon(data)

    # Save compressed version
    with open(f"compressed/{file.stem}.toon", "w") as f:
        f.write(toon)
```

## Troubleshooting

### Import Error

```bash
# Make sure you're in the right directory
cd JSON2TOON

# Reinstall
pip install -e .
```

### MCP Server Not Starting

```bash
# Check Python version
python --version  # Should be 3.10+

# Check MCP installation
pip list | grep mcp

# Reinstall MCP
pip install mcp>=0.9.0
```

### Tests Failing

```bash
# Install test dependencies
pip install -e ".[dev]"

# Run tests with verbose output
pytest tests/ -v -s
```

## Next Steps

1. **Read the full README**: [README.md](README.md)
2. **Explore examples**: `python examples/basic_usage.py`
3. **Run tests**: `pytest tests/ -v`
4. **Try MCP tools** in Claude
5. **Experiment** with different compression levels

## Performance Tips

✅ **Use STANDARD for most cases** - Best balance
✅ **Use AGGRESSIVE for large datasets** - High savings
✅ **Use EXTREME for archival** - Maximum compression
✅ **Analyze patterns first** - Optimize strategy
✅ **Batch process** when possible - Better performance

## Key Features

- 🎯 **4 compression levels** (30% to 85% savings)
- 🤖 **17+ pattern types** detected automatically
- 🔧 **12 MCP tools** for Claude integration
- 📊 **Real-time metrics** and analysis
- ✅ **100% lossless** round-trip conversion

## Support

- 📖 **Full docs**: See [README.md](README.md)
- 🐛 **Issues**: GitHub Issues
- 💬 **Questions**: GitHub Discussions
- 📧 **Contact**: See project maintainers

---

**Ready to save tokens?** 🎉

```bash
python examples/basic_usage.py
```

Happy compressing!
