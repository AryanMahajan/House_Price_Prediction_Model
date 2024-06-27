**House Price Prediction with TensorFlow and Keras**
This repository contains code for a project that predicts house prices based on three features: area, number of bedrooms, and number of bathrooms. It utilizes the TensorFlow library with the Keras high-level API for building and training the machine learning model.

**Project Overview**
This project implements a simple regression model to predict house prices. Here's a breakdown of the steps involved:


**Data Loading and Preprocessing:**
Load a CSV dataset containing house information (area, bedrooms, bathrooms, and price).
Handle missing values (if any) through techniques like imputation or removal.
Encode categorical features (if present) using techniques like one-hot encoding.
Normalize numerical features (area, bedrooms, bathrooms) for better model performance.

**Model Building:**
Define a sequential Keras model with dense layers.
Choose an appropriate activation function (e.g., ReLU) for hidden layers.
Specify the output layer with a single neuron for price prediction.

**Model Training:**
Compile the model with a suitable loss function (e.g., mean squared error) and optimizer (e.g., Adam).
Split the data into training and testing sets.
Train the model on the training set for a specific number of epochs.

**Model Evaluation:**
Evaluate the model's performance on the testing set using metrics like mean squared error or R-squared.
Optionally, visualize the predicted vs. actual prices for insights.


**Dependencies**
This project requires the following Python libraries:

TensorFlow

Keras

Pandas (for data manipulation)

NumPy (for numerical computations)

**How to run the model:**
1. After downloading or cloning the repository. Go to the "main.py" file.
2. Then go to the terminal and type "python main.py" to run the model and make a prediction.

**Inbuilt model**
The model "model.keras" is already trained on a dataset of 1461 examples.

**Contributor: Aryan Mahajan**
**GitHub Username: AryanMahajan**
