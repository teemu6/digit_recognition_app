# Build stage
FROM python:3.8-slim-buster AS build

# Set the working directory to /app
WORKDIR /digit_recognition_microservice

# Copy the current directory contents into the container at /app
COPY . /digit_recognition_microservice

# Create a virtual environment
RUN python -m venv /venv

# Activate the virtual environment
ENV PATH="/venv/bin:$PATH"

# Upgrade pip to the latest version
RUN /venv/bin/python -m pip install --upgrade pip

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-dev

# Install any needed packages specified in requirements.txt
RUN /venv/bin/python -m  pip install --no-cache-dir -r requirements.txt

# Upgrade TensorFlow and Keras to the latest versions
RUN /venv/bin/python -m  pip install --upgrade tensorflow keras

# Production stage
FROM python:3.8-slim-buster

# Copy the installed packages from the build stage
COPY --from=build /venv /venv

# Set the working directory to /digit_recognition_microservice
WORKDIR /digit_recognition_microservice

# Copy the current directory contents into the container at /digit_recognition_microservice
COPY . /digit_recognition_microservice

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-dev

# Activate the virtual environment
ENV PATH="/venv/bin:$PATH"

# Expose port 5005 for the Flask app
EXPOSE 5005

# Run the app using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5005", "digit_recognition_microservice:app"]