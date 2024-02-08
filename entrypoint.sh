#!/bin/ash
echo "Applying Database Migration"
python manahe.py makemigrations
python manage.py migrate
exec "$@"
# python manage.py collectstatic --no-input