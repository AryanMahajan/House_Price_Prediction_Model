from loading_data import create_train_data

import tensorflow as tf
import pickle
import os
import numpy as np

if os.path.exists("X_train.pickle") and os.path.exists("y_train.pickle"):
    print("LOADING TRAINING DATA")
    x_train = pickle.load(open("X_train.pickle", "rb"))
    y_train = pickle.load(open("y_train.pickle", "rb"))
else:
    create_train_data()
    print("LOADING TRAINING DATA")
    x_train = pickle.load(open("X_train.pickle", "rb"))
    y_train = pickle.load(open("y_train.pickle", "rb"))


def training_model():

    model = tf.keras.Sequential([])
    model.add(tf.keras.layers.Dense(units=1))
    model.compile(optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.001),loss='mse')
    model.fit(np.array(x_train), np.array(y_train), epochs = 30, validation_split = 0.3)
    model.save("model.keras")