# my_hello_app/Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Define a build argument for the image tag
ARG IMAGE_TAG

# Set an environment variable in the container using the build argument's value
ENV APP_IMAGE_TAG=${IMAGE_TAG}

# Set the working directory in the container
WORKDIR /app

COPY cicd/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
# Copy the current directory contents into the container at /app
COPY cicd/main.py /app/main.py

# Run main.py when the container launches
CMD ["python", "main.py"]
