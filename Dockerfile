FROM alpine:latest

RUN apk add --no-cache git curl jq openssh

# Аргументы/переменные
ENV GITLAB_GROUP_PATH=barbariki245
ENV GITLAB_API_TOKEN=glpat-KY81g4JLGxgjs1wr1CR6
ENV GITLAB_API_URL=https://gitlab.com/api/v4

WORKDIR /projects

# Клонирование всех репозиториев группы
RUN curl --silent --header "PRIVATE-TOKEN: $GITLAB_API_TOKEN" "$GITLAB_API_URL/groups/$GITLAB_GROUP_PATH/projects?per_page=100" \
    jq -r '.[].path_with_namespace' | while read repo; do \
      git clone "https://oauth2:${GITLAB_API_TOKEN}@gitlab.com/${repo}.git"; \
    done

    | while read repo; do \
        git clone "$repo"; \
    done
