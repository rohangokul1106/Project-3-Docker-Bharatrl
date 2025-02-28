FROM python:3.9-alpine

# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /home/data

# Copy script and text files into the container
COPY scripts.py .
COPY IF-1.txt .
COPY AlwaysRememberUsThisWay-1.txt .

# Run the Python script automatically when the container starts
CMD ["python", "scripts.py"]

