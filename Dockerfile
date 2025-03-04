# Use an official Python runtime as base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy project files to the container
COPY requirements.txt requirements.txt
COPY app.py app.py

# Install dependencies
RUN pip install -r requirements.txt

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
