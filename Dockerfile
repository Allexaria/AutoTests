# Базовый образ
FROM python:3.11-slim

# Рабочая директория
WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
ENV PYTHONPATH=/app
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходников и тестов
COPY . /app

# Команда по умолчанию
CMD ["pytest"]
