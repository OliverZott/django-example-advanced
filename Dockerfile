FROM python:3.11.1-alpine3.17

LABEL maintainer="dasmuesli"

# prevent delays: see logs immediatly
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
# to connect to django dev server
EXPOSE 8000

# default value; Overwritten by docker-compose.yml
ARG DEV=false

# virtual env on docker image... not really necessary
# BEST PRACTICE - add user to not use root-user ->  security issues!
# BEST PRACTICE - keep lightweight as possible (remove unused stuff)!
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /venv/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
#    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user 


# to have python commands without using full path
ENV PATH="/venv/bin:$PATH"

# switch to new user
USER django-user
