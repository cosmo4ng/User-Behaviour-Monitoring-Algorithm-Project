
"""AI_for_Monitoring_User_Behaviour.ipynb

Automatically generated by Colaboratory.

Original file is located at
  https://colab.research.google.com/drive/12ShGyRPBuseUsQ-ORP01iehB3MUcCEfK#scrollTo=Z7be-4wZ8zuO

Import the dataset.

[Click here for the dataset](https://gist.github.com/cosmo4ng/b56c3b762183589e23dbe2bc4f2c33ed)
"""

import pandas as pd

dataset = pd.read_csv('user_behaviour.csv')

x = dataset.drop(columns=["behaviour(1=b 0=g)"])

y = dataset["behaviour(1=b 0=g)"]

"""Split the data into a training set and a testing set."""

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

"""Build and train the model."""

import tensorflow as tf

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Dense(256, input_shape=x_train.shape, activation='sigmoid'))
model.add(tf.keras.layers.Dense(256, activation='sigmoid'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=1000)

"""Evaluate the model."""

model.evaluate(x_test, y_test)

