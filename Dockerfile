# Use a base image
FROM python:3.10-slim-buster

# Set working directory
WORKDIR /app

# Copy app files into the container
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .


# Command to run the app
CMD ["python", "app.py"]
