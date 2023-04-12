import numpy as np
import cv2
import keras.models as models
from flask import Flask, request, jsonify

# load the model
model = models.load_model('mymodel')

# initialize the Flask app
app = Flask(__name__)

def preprocess_image(img):
    # resize the input image to a fixed size of 28x28 pixels
    img = cv2.resize(img, (28,28))
    
    # invert the image colors
    img = cv2.bitwise_not(img)
    
    # normalize the pixel values to be between -0.5 and 0.5
    img = (img / 255) - 0.5
    
    # add an extra dimension to the image tensor to represent a batch of size 1
    img_tensor = np.expand_dims(img, axis=0)
    
    # return the preprocessed image tensor
    return img_tensor

def segment_image(img):
    # Threshold the image
    _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Sort contours from left to right
    contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[0])
    
    # Extract each digit and predict class id
    predictions = []
    
    for cnt in contours:
        # Get the bounding rectangle coordinates for the contour
        x,y,w,h = cv2.boundingRect(cnt)
        
        # Crop the digit from the original image using the bounding rectangle coordinates
        digit = img[y:y+h, x:x+w]
        
        # Add white padding around the digit
        digit = cv2.copyMakeBorder(digit, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[255, 255, 255])
        
        # Preprocess the digit image for prediction
        digit = preprocess_image(digit)
        
        # Make a prediction for the digit image using the pre-trained model
        prediction = model.predict(digit)
        
        # Get the predicted class ID for the digit image
        class_id = np.argmax(prediction)
        
        # Append the predicted class ID to the list of predictions
        predictions.append(int(class_id))
        
    return predictions

@app.route('/predict', methods=['POST'])
def predict_number():
    # get the image from the POST request
    img_file = request.files['image']

    # convert file object to bytes
    img_bytes = img_file.read()

    # convert bytes to numpy array
    img_array = np.frombuffer(img_bytes, np.uint8)

    # decode image
    img = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)

    # segment image into individual digits
    predictions = segment_image(img)

    # make a prediction and return the result as JSON
    response = {'class_ids': predictions}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
