FROM python:3.11-slim

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


RUN pip install -e ./pages

CMD ["pytest"]
