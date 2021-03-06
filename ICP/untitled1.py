# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1893emNBgALUjL3j1YR2su3DgG_nTpHoj
"""

import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv("/content/drive/My Drive/ICP-6/icp-1/Breas Cancer.csv")
classes = ['Benign', 'Malignant']
X = dataset.iloc[:, 2:32].values
y = dataset.iloc[:, 1].values
from sklearn.preprocessing import LabelEncoder
labelencoder_X_1 = LabelEncoder()
y = labelencoder_X_1.fit_transform(y)
print(y)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
my_first_nn = Sequential() # create model
my_first_nn.add(Dense(8, input_dim=30, activation='relu')) # hidden layer
my_first_nn.add(Dense(20, input_dim=30, activation='relu')) # hidden layer
my_first_nn.add(Dense(50, input_dim=30, activation='relu')) # hidden layer
my_first_nn.add(Dense(80, input_dim=30, activation='relu'))
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
my_first_nn_fitted = my_first_nn.fit(X_train, y_train, epochs=100, verbose=0,
                                     initial_epoch=0)
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, y_test, verbose=0))

import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation
import warnings
warnings.filterwarnings('ignore')

# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd
dataset = pd.read_csv("/content/drive/My Drive/ICP-6/icp-1/diabetes.csv", header=None).values
# print(dataset)
import numpy as np
X_train, X_test, Y_train, Y_test = train_test_split(dataset[:,0:8], dataset[:,8],
                                                    test_size=0.25, random_state=87)
np.random.seed(155)
my_first_nn = Sequential() # create model
my_first_nn.add(Dense(20, input_dim=8, activation='relu')) # hidden layer
my_first_nn.add(Dense(90, input_dim=8,  activation='relu')) # hidden layer
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam')
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100, verbose=0,
                                     initial_epoch=0)
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test, verbose=0))