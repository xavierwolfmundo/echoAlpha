# Use the official Python image as the base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq-dev

# Install Python dependencies
COPY requirements.txt /usr/src/app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the Django project files to the container
COPY . /usr/src/app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Run Django application on port 8000
CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
