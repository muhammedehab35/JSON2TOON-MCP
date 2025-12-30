# JSON2TOON MCP Server - Optimized Docker Image
FROM python:3.11-slim

# Metadata
LABEL maintainer="JSON2TOON Team"
LABEL version="2.0.0"
LABEL description="Advanced Token-Optimized Object Notation MCP Server"

# Set working directory
WORKDIR /app

# Set environment variables for Python optimization
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONOPTIMIZE=2

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files first (for better Docker layer caching)
COPY requirements.txt pyproject.toml ./

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -e .

# Copy application source code
COPY src/ ./src/
COPY tests/ ./tests/
COPY examples/ ./examples/

# Create non-root user for security
RUN useradd -m -u 1000 json2toon && \
    chown -R json2toon:json2toon /app

# Switch to non-root user
USER json2toon

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; from src.advanced_converter import AdvancedTOONConverter; sys.exit(0)"

# Expose port (if needed for future HTTP interface)
# EXPOSE 8000

# Run the MCP server
CMD ["python", "-m", "src.mcp_server"]
