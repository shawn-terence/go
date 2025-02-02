# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install gcc, libcups2-dev, and other necessary build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libc-dev \
    build-essential \
    pkg-config \
    libcairo2-dev \
    python3-dev \
    libgirepository1.0-dev \
    libsystemd-dev \
    libcups2-dev \
    libdbus-1-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code to the container
COPY . /app/

# Expose the port that the Django app runs on
EXPOSE 8000

# Define environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]