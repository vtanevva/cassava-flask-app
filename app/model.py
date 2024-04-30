import keras
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import pandas as pd
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


# Load your trained model
model = load_model('efficient.keras')
model.summary()

preds = []
test_image = 'app/static/test_image/cmd.jpg' #here, you can put the image whose class you want to predict 
dir = 'app/challenge/'

from keras.preprocessing.image import img_to_array, smart_resize
import numpy as np

def predict(model, img):
    # Assuming img is a PIL image, preprocess it
    img = img_to_array(img)  # Convert PIL image to a numpy array
    img = smart_resize(img, (224, 224))  # Resize image if needed
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    prediction = model.predict(img)
    predicted_label = np.argmax(prediction, axis=1)[0]
    return predicted_label




# my_submission = pd.DataFrame({'image_id': ss.image_id, 'label': preds})
# my_submission.to_csv('submission.csv', index=False) 
# return my_submission

 