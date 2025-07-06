# Базовый образ
FROM python:3.11-slim

# Установка зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code and tests
COPY . .

# Команда по умолчанию
CMD ["pytest"]