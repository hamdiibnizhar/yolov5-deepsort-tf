import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image

New_Model = tf.keras.models.load_model('yolo4.h5') # Loading the Tensorflow Saved Model (PB)
print(New_Model.summary())

# New_Model.save('New_Model.h5') # Saving the Model in H5 Format

# loaded_model_from_h5 = tf.keras.models.load_model('New_Model.h5') # Loading the H5 Saved Model
# print(loaded_model_from_h5.summary())