FROM python:3.12-slim

WORKDIR /app

# Install Poetry
RUN pip install poetry==1.8.3

# Copy poetry configuration files
COPY pyproject.toml poetry.lock* /app/

# Configure poetry to not use a virtual environment
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-interaction --no-ansi

# Copy the application
COPY . /app/

# Run the application
CMD ["python", "-m", "app.main"]