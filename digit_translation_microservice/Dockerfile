# Use an official Node.js runtime as a parent image
FROM node:14-alpine

# Set the working directory to /digit_translation_microservice
WORKDIR /digit_translation_microservice

# Copy the current directory contents into the container at /digit_translation_microservice
COPY . /digit_translation_microservice

# Install any needed packages specified in package.json
RUN npm install

# Expose port 5006 for the Node.js app
EXPOSE 5006

# Run index.js when the container launches
CMD ["node", "index.js"]