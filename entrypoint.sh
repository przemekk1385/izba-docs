#!/bin/sh

until nc -z -v -w30 $DJ_DATABASE_HOST $DJ_DATABASE_PORT
do
  echo "Waiting for database connection..."
  sleep 5
done

python ./manage.py migrate
python ./manage.py collectstatic --no-input

exec "$@"
