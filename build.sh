#!/bin/bash

# Stop execution if any command fails
set -e

echo "🔹 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🔹 Applying migrations..."
python manage.py migrate

echo "🔹 Collecting static files..."
python manage.py collectstatic --noinput

echo "✅ Build script completed successfully!"
