# The base image
FROM python:3.9.6

# Create app directory
WORKDIR /app

# Install ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install your application's dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y git
RUN pip install --no-cache-dir -r requirements.txt
