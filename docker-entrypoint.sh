#!/bin/sh

set -e

if [ ! -z "$DATABASE_URL" ]
then
    until psql $DATABASE_URL -c '\l'; do
      >&2 echo "Postgres is unavailable - sleeping"
      sleep 1
    done

    >&2 echo "Postgres is up - continuing"
fi

# Apply database migrations
/venv/bin/python manage.py migrate

# Collect static files
/venv/bin/python manage.py collectstatic --noinput

echo "from django.contrib.auth.models import User; User.objects.create_superuser('${DJANGO_ADMIN_USERNAME}', '${DJANGO_ADMIN_EMAIL}', '${DJANGO_ADMIN_PASSWORD}')" | /venv/bin/python manage.py shell

/venv/bin/uwsgi --ini /code/uwsgi.test.ini