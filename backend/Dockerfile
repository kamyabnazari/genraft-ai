# Dockerfile for Generaft AI Backend
FROM python:3.10

# Set environment variable
ENV XDG_RUNTIME_DIR=/tmp/runtime-root

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    pkg-config && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the local src files to the container
ADD . /app

# Install python dependencies
RUN pip install -r requirements.txt --no-cache-dir

# Expose port for the application
EXPOSE 5003

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5003"]
