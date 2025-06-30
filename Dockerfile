# Use a slim official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app source code from folder todo
COPY . .

# Make sure the DB file (if it exists locally) is copied in
COPY instance/todo.db ./todo.db

# Expose Flask port
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Command to run the app
CMD ["python", "run.py"]
