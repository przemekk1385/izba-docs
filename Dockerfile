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


FROM builder AS prod

RUN poetry install --no-dev


FROM builder AS dev

RUN apt-get install -y vim

RUN poetry install
