# Use Alpine base with Python 3
FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Copy Python script into container
COPY pokemon_scanner.py .

# Install dependencies
RUN pip install requests

# Default command (can override at runtime)
ENTRYPOINT ["python", "pokemon_scanner.py"]

