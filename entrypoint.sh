#!/bin/sh
echo "Apply Database Migration"
python manage.py migrate --no-input
python manage.py collectstatic --no-input