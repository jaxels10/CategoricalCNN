from keras.models import load_model
import numpy as np

classifier = load_model('categoricalModel.h5')

from keras.preprocessing import image

# Insert image path below for the image you want to test on the neural network

np.set_printoptions(suppress=True)
test_image = image.load_img('YourIMGPathHere', target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = test_image/255
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict_proba(test_image)


print(result[0])
