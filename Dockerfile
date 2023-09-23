# Use the official Python image as the base image
FROM python:3.8

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the Django application into the container
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Start Gunicorn to run the Django application
CMD ["gunicorn", "copypasta_celery.wsgi:application", "-b", "0.0.0.0:8000"]
