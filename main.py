from loading_data import create_test_data
from training_model import training_model

import tensorflow as tf
import os
import pickle
import numpy as np

#Checking if the model exists or not
if os.path.exists("model.keras"):
    print("Model exists")
    model = tf.keras.models.load_model("model.keras")
else:
    print("Training Model")
    training_model()
    model = tf.keras.models.load_model("model.keras")

#Checking if the data is saved or not
if os.path.exists("X_test.pickle") and os.path.exists("y_test.pickle"):
    print("LOADING TEST DATA")
    x_test = np.array(pickle.load(open("X_test.pickle", "rb")))
    y_test = np.array(pickle.load(open("y_test.pickle", "rb")))
else:
    create_test_data()
    print("LOADING TEST DATA")
    x_test = np.array(pickle.load(open("X_test.pickle", "rb")))
    y_test = np.array(pickle.load(open("y_test.pickle", "rb")))

preditction = []

prediction = model.predict([x_test])
print(prediction*10)
os.remove('X_test.pickle')
os.remove('y_test.pickle')