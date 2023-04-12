# Weekly Scrum - Progress report

## Week 1

### Last week(s)

- Played around with neural network examples provided by teacher. Got the provided codes working, had to install bunch of libraries and python.
- Created a Translator service using Azure Cognitive Services and made a python app to test the API, which worked fine to for translating text from one language to another.
- Created an python API using Flask framework, that accepts image blobs in it's POST endpoint. The API uses keras library and has already trained model that is loaded during startup. It then tries to predict the single digit number that is displayed in the image and sends back a number as a response.
- Created a frontend web app, where the user can upload an image from his computer, or draw a number on HTML canvas element. The images can be sent to the API for prediction and the web app will show the predicted number. Styled it using Bootstrap framework.
- Web app and the image prediction API works together locally (will bother with microservices, docker containers and such later)

### Current activities

- Trying to look for a way to read multiple digits from image.

### Next week

- If it seems doable without crazy effort, will try to implement the reading of multiple digits from image. Otherwise I will work on Cognitive services to turn digits to written words and see if I can get API for that up and running.
