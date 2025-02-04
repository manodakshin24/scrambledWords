# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY scrambledWordScript.py .

# Install any necessary dependencies (if needed)
# For this script, no additional dependencies are required.

# Run the script when the container starts
CMD ["python", "scrambledWordScript.py"]