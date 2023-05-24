# Digit Recognition Microservice

This microservice provides an API for recognizing handwritten digits. It is implemented using Python and Flask, and uses a convolutional neural network (CNN) model to recognize the digits.

## Technical Description

The CNN model comes pre-trained with around 60k images of different digits. The model data is localed in "mymodel"-folder.

The microservice provides a single endpoint for recognizing digits from an image file "/recognizeimage", which is invoked using HTTP request POST method, where the image file (png, bmp, jpg, etc.) is passed in the request files object. The image will then be processed, the digits will be segmented into smaller parts, fed to the CNN model, that will then try to recognize the digit one by one. The results will be sent back as an array of numbers (e.g. [6,7,8,9]) as response to the client.

## Requirements

To run the digit recognition microservice locally, you will need the following software installed:

- [Docker](https://www.docker.com/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

## Usage

As the model is pretrained, you don't have to do it necessarily, but if you want to do it again, just run the Python program that trains it (be sure to install Python and the dependencies first): 
`python train_model_with_number_images.py`

Here are the steps to deploy the microservice:

1. Point your terminal's docker cli to the Docker Engine inside Minikube: `minikube docker-env`
2. Build the microservice image, it will be around 2.3 Gb in size: `docker build -t digit_recognition_microservice:latest .`
3. Deploy the container along with a Service: `kubectl apply -f deployment.yaml`

See also [instructions in main README](../README.md) how to setup the other microservices and the ingress.