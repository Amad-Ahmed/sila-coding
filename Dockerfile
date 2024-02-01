FROM python:3.11.0-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && apt-get clean

# Copy the application files to the container
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0","--reload"]

EXPOSE 8000

