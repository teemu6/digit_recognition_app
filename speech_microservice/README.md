# Speech Microservice

This microservice provides an API for converting text to speech (audio file). It is implemented using Node.js, Express framework and Azure Cognitive services Speech service.

## Technical Description

The microservice provides a single endpoint for converting text to speech "/text-to-speech", which is invoked using HTTP request POST method, with "languageCode" and "text" in the request body. The microservice uses "microsoft-cognitiveservices-speech-sdk" library internally to connect Azure Speech service, where the specified parameters are used to get an mp3 audio stream. It is then base64 encoded and forwarded to the client as response.

## Requirements

To run the digit recognition microservice locally, you will need the following software installed:

- [Docker](https://www.docker.com/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

You will also need to have Azure subscription and Speech service set up, as the microservice will use it for generating the audio files. Check the official [documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/).

## Usage

Here are the steps to deploy the microservice:

1. Modify [.env file](./.env) with your Azure Speech service access key and location. You can find these information from Azure after the resource is created. The node app will fetch these values on runtime.
2. Point your terminal's docker cli to the Docker Engine inside Minikube: `minikube docker-env`
3. Build the microservice image, it will be around 220 Mb in size: `docker build -t speech_microservice:latest .`
4. Deploy the container along with a Service: `kubectl apply -f deployment.yaml`

See also [instructions in main README](../README.md) how to setup the other microservices and the ingress.