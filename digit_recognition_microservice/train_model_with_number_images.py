import numpy as np
import mnist
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from keras.utils import to_categorical
from keras.optimizers import SGD

train_images = mnist.train_images()#[:5000]
train_labels = mnist.train_labels()#[:5000]
test_images = mnist.test_images()#[:5000]
test_labels = mnist.test_labels()#[:5000]

train_images = (train_images / 255) - 0.5
test_images = (test_images / 255) - 0.5

train_images = np.expand_dims(train_images, axis=3)
test_images = np.expand_dims(test_images, axis=3)

model = Sequential([
 Conv2D(8, 3, input_shape=(28, 28, 1), use_bias=False),
 MaxPooling2D(pool_size=2),
 Flatten(),
 Dense(10, activation='softmax'),
])

model.compile(SGD(lr=.005), loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(
 train_images,
 to_categorical(train_labels),
 batch_size=1,
 epochs=3,
 validation_data=(test_images, to_categorical(test_labels)),
)

# Save the model
model.save('mymodel')