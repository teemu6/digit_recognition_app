# Use an official Node.js runtime as a parent image
FROM node:14-alpine

# Set the working directory to /speech-microservice
WORKDIR /speech-microservice

# Copy the current directory contents into the container at /speech-microservice
COPY . /speech-microservice

# Install any needed packages specified in package.json
RUN npm install

# Expose port 5007 for the Node.js app
EXPOSE 5007

# Run index.js when the container launches
CMD ["node", "index.js"]