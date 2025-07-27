# Use official Python image
FROM python:3.11-slim-bullseye

# Set working directory
WORKDIR /app

# Copy all files to /app in container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]
