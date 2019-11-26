# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:14:54 2019

@author: Gabriel Carvalho
"""
'''
=======================================================================================================

                                    Landmark Recognition

-------------------------------------------------------------------------------------------------------
'''
#Importing the libraries needed
import numpy as np
import matplotlib.pyplot as plt
import cv2
import tensorflow as tf
import pickle


# Loading the model
model = tf.keras.models.load_model("Conv Net MK39")

# Loading the training dataset
X_train = pickle.load(open("X.pickle", "rb"))
y_train = pickle.load(open("y.pickle", "rb"))

# Normalizing the image
X_train = X_train/255.0


# Training the model
history = model.fit(X_train, y_train, validation_split=0.25, epochs=50, batch_size=16, verbose=1)

# Plot training & validation accuracy values
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()


# Saving the model
model.save("Conv Net MK39")

# Loading the testing dataset
pickle_in = open("X_test.pickle", "rb")
X_test = pickle.load(pickle_in)
X_test = tf.cast(X_test, tf.float32)

pickle_in = open("y_test.pickle", "rb")
y_test = pickle.load(pickle_in)

# Normalizing the test dataset
X_test = X_test/255.
y_test = y_test


