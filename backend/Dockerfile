FROM python:3.11-slim
WORKDIR /app

# Copy dependency specs & install Poetry
COPY pyproject.toml poetry.lock* /app/
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --only=main --no-root

# Copy your application code
COPY . /app

# Run the application
CMD ["poetry", "run", "python", "app.py"]