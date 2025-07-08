FROM python:3.12-alpine


RUN apk add --no-cache git curl jq openssh

# Аргументы/переменные
ENV GITLAB_GROUP_PATH=barbariki245
ENV GITLAB_API_TOKEN=glpat-KY81g4JLGxgjs1wr1CR6
ENV GITLAB_API_URL=https://gitlab.com/api/v4

WORKDIR /projects

COPY requirements.txt /projects/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Клонирование всех репозиториев группы
RUN curl --silent --header "PRIVATE-TOKEN: $GITLAB_API_TOKEN" \
    "$GITLAB_API_URL/groups/$GITLAB_GROUP_PATH/projects?per_page=100" \
    | jq -r '.[].path_with_namespace' \
    | while read repo; do \
        git clone "https://oauth2:${GITLAB_API_TOKEN}@gitlab.com/${repo}.git"; \
      done

# установка Allure
RUN curl -o allure.zip -L https://github.com/allure-framework/allure2/releases/download/2.34.0/allure-2.34.0.zip && \
    unzip allure.zip -d /opt/ && \
    ln -s /opt/allure-2.34.0/bin/allure /usr/bin/allure && \
    rm allure.zip

# запуск тестов при запуске контейнера
CMD ["pytest", "tests", "--alluredir=allure-results"]
