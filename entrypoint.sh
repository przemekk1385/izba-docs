#!/bin/sh

until nc -z -v -w30 $COMPOSE_DATABASE_HOST $COMPOSE_DATABASE_PORT
do
  echo "Waiting for database connection..."
  sleep 5
done

python ./manage.py migrate
python ./manage.py collectstatic --no-input

exec "$@"
