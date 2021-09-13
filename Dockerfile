FROM python:3.9-slim-buster AS builder

ENV VIRTUAL_ENV=/usr/local/python

RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apt-get update \
    && apt-get install -y netcat

RUN python -m pip install --upgrade pip
RUN pip install poetry

WORKDIR /code

COPY . /code/


FROM builder AS prod

RUN poetry install --no-dev

ENTRYPOINT ["/code/entrypoint.sh"]


FROM builder AS dev

RUN poetry install

ENTRYPOINT ["/code/entrypoint.sh"]
