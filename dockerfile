# Use slim variant → smaller image, still has what we need
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies first → better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Environment variables can come from docker-compose or .env
ENV PYTHONUNBUFFERED=1

# Default command — can be overridden in docker-compose
CMD ["python", "-m", "src.pipeline"]