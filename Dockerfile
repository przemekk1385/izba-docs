FROM python:3.9-buster

ENV VIRTUAL_ENV=/usr/local/env

RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apt-get update \
    && apt-get install -y vim netcat
RUN python -m pip install --upgrade pip

RUN pip install poetry \
    && poetry config virtualenvs.create false

WORKDIR /usr/local/src/app

COPY ./izba_docs ./izba_docs
COPY ./izba_docs_api ./izba_docs_api
COPY ./manage.py .

COPY ./pyproject.toml .
COPY ./poetry.lock .

COPY ./entrypoint.sh .
COPY ./.env .

RUN poetry install --no-dev

EXPOSE 8000

ENTRYPOINT ["/usr/local/src/app/entrypoint.sh"]
