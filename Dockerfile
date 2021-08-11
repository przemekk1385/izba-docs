FROM python:3.9-slim AS builder

ENV VIRTUAL_ENV=/usr/local/env

RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apt-get update \
    && apt-get install -y netcat
RUN python -m pip install --upgrade pip
RUN pip install poetry

WORKDIR /code

COPY . /code/

ENTRYPOINT ["/code/entrypoint.sh"]


FROM builder AS dev

RUN apt-get install -y vim git

ARG GIT_USER_NAME
RUN git config --global user.name "${GIT_USER_NAME}"

ARG GIT_USER_EMAIL
RUN git config --global user.email ${GIT_USER_EMAIL}

RUN poetry install


FROM builder AS prod

RUN poetry install --no-dev
