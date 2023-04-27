# Weekly Scrum - Progress report

## Week 1

### Last week(s)

- Played around with neural network examples provided by teacher. Got the provided codes working, had to install bunch of libraries and python.
- Created a Translator service using Azure Cognitive Services and made a python app to test the API, which worked fine to for translating text from one language to another.
- Created an python API using Flask framework, that accepts image blobs in it's POST endpoint. The API uses keras library and has already trained model that is loaded during startup. It then tries to predict the single digit number that is displayed in the image and sends back a number as a response.
- Created a frontend web app, where the user can upload an image from his computer, or draw a number on HTML canvas element. The images can be sent to the API for prediction and the web app will show the predicted number. Styled it using Bootstrap framework.
- Web app and the image prediction API works together locally (will bother with microservices, docker containers and such later)

### This week

- Trying to look for a way to read multiple digits from image.

### Next week

- If it seems doable without crazy effort, will try to implement the reading of multiple digits from image. Otherwise I will work on Cognitive services to turn digits to written words and see if I can get API for that up and running.

## Week 2

### Last week

- Modified the digit recognition service, so that it looks for multiple digits in the image, then does process called "segmentation" to make a prediction for each digit in its own segment, then combine it as an array of numbers. Had to add some white padding to the segments around the digits, because the model was trained with images that had it too, so it was necessary thing to do or the model did not recognize the digits.
- Modified also the frontend web app, so that the canvas to draw numbers is wider for making easier to write multiple digits. The API response was now an array of numbers, so modified the client side to accept that type of response

### This week

- Working on making a microservice, that will turn digits into english written numbers, such as 25 -> "twenty-five".
- Maybe if I have time I will then do another service that does translations to other languages, using Azure cognitive services.

### Next week

- Will work on making the rest microservices, such as translation or text to speech

## Week 3

- Sorry dear Scrum Team, I was on a vacation and couldn't do anything useful. No progress

## Week 4

### This week

- Created a digit translation service, using node.js and express library. For now it is just an API with endpoint, that uses GET method where the user will provide the number and a language code as a query parameter. It will then convert the number to an english written number using "number-to-words" npm package. This english word will be then sent to Azure Cognitive Services Translator service I created in the Azure. The API will then return the translated text as response. For example if I request the endpoint with "/translate?number=123&langCode=fi" I will get a response "sata kaksikymmentäkolme". I will turn this API later on to a real microservice
- Will try to see if I can implement the frontend app to use this API

### Next week

- Digit translation API integration with the frontend app, maybe add an option for the user to define language code in the UI that will be used in the translation along with the uploaded/drawn picture
