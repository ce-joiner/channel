FROM python:3.11-slim
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency specs
COPY pyproject.toml poetry.lock /app/

# Install Poetry and dependencies
RUN pip install "poetry==1.7.1" \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --only main

# Copy application code
COPY . /app

# Run the application
CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]