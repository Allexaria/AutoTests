# AutomationExercise: pytest + Selenium (Chromium) + optional Allure CLI for HTML from raw results.
# Build from repository root:  docker build -t ae-tests .

FROM python:3.11-slim-bookworm

# CHROME_BIN: packaged Chromium. SELENIUM_HEADLESS: required in container (no display).
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    CHROME_BIN=/usr/bin/chromium \
    SELENIUM_HEADLESS=1

WORKDIR /app

# Browser, Java (for Allure CLI), and minimal fonts for page rendering
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    ca-certificates \
    chromium \
    chromium-driver \
    curl \
    fontconfig \
    fonts-liberation \
    openjdk-17-jre-headless \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Pin Allure 2 (HTML from --alluredir; separate from allure-pytest)
ARG ALLURE_VERSION=2.34.0
RUN curl -fsSL -o /tmp/allure.zip \
    "https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.zip" \
    && unzip -q /tmp/allure.zip -d /opt/ \
    && ln -sf "/opt/allure-${ALLURE_VERSION}/bin/allure" /usr/local/bin/allure \
    && rm -f /tmp/allure.zip

# Install Python deps (root requirements includes AutoTests list)
COPY requirements.txt ./requirements.txt
COPY AutoTests-abobatests/requirements.txt ./AutoTests-abobatests/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Project sources (see .dockerignore)
COPY . .

# Default: UI + API tests; override CMD for markers or path
CMD ["pytest", "AutoTests-abobatests/tests", "-q", "--alluredir=allure-results"]
