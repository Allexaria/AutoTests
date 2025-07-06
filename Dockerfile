FROM python:3.11-slim

WORKDIR /app

# Клонируем первый проект
RUN git clone https://gitlab.com/barbariki245/test-selenium
# Клонируем второй проект
RUN git clone https://gitlab.com/barbariki245/automation.framework

# Устанавливаем зависимости только из основного проекта
RUN pip install --no-cache-dir -r main-project/requirements.txt

CMD ["pytest"]