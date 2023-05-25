# Digit Translation Microservice

This microservice provides an API for translating ordinal number (digits) to a written version in a specified language. It is implemented using Node.js, Express framework and Azure Cognitive services Translator.

## Technical Description

The microservice provides a single endpoint for translation from an ordinal number "/translate", which is invoked using HTTP request GET method, with the number and language code as query parameters. The number is converted to a english written number using "number-to-words" JS library. For example if the query parameter "number" is "123" and "langCode" is "fi", the number is converted to "one hundred and twenty-three". This string is then sent to Azure Cognitive Services Translator Service, along with the language code, which returns "sata kaksikymmentäkolme". It will be forwarded back to the client as response.

## Requirements

To run the digit recognition microservice locally, you will need the following software installed:

- [Docker](https://www.docker.com/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

You will also need to have Azure subscription and Translator service set up, as the microservice will use it for the translations. Check the official [documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/translator/).

## Usage

Here are the steps to deploy the microservice:

1. Modify [.env file](./.env) with your Azure Translator service access key, endpoint and location. You can find these information from Azure after the resource is created. The node app will fetch these values on runtime.
2. Point your terminal's docker cli to the Docker Engine inside Minikube: `minikube docker-env`
3. Build the microservice image, it will be around 220 Mb in size: `docker build -t digit_translation_microservice:latest .`
4. Deploy the container along with a Service: `kubectl apply -f deployment.yaml`

See also [instructions in main README](../README.md) how to setup the other microservices and the ingress.