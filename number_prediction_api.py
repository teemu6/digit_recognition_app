import numpy as np
import cv2
import keras.models as models
from flask import Flask, request, jsonify

# load the model
model = models.load_model('mymodel')

# initialize the Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_number():
    img_file = request.files['image']

    # convert file object to bytes
    img_bytes = img_file.read()

    # convert bytes to numpy array
    img_array = np.frombuffer(img_bytes, np.uint8)

    # decode image
    img = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)

    img = cv2.resize(img, (28,28))
    img = cv2.bitwise_not(img)
    img = (img / 255) - 0.5
    img_tensor = np.expand_dims(img, axis=0)

    # make a prediction and return the result as JSON
    prediction = model.predict(img_tensor)
    class_id = np.argmax(prediction)
    response = {'class_id': int(class_id)}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
