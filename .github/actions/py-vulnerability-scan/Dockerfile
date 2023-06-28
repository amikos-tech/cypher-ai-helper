FROM python:3.10-alpine AS base-action

LABEL maintainer="Trayn Azarov <trayan.azarov@chaoslabs.io>"


RUN apk add --no-cache github-cli && \
    pip3 install -U setuptools pip bandit

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["sh","/entrypoint.sh"]
