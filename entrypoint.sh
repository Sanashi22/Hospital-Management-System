#!/bin/ash
echo "Applying Database Migration"
python manage.py makemigrations
python manage.py migrate
exec "$@"
# python manage.py collectstatic --no-input