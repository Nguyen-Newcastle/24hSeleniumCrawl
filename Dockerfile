# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 4444 for Selenium Grid
EXPOSE 4444

# Default command to run your script (can be overridden by Docker Compose)
CMD ["python", "/app/scripts/extract_latest_articles_on_sections.py"]
