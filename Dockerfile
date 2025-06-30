# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Expose port Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
