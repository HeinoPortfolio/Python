# -*- coding: utf-8 -*-
"""
Created on Tue May 23 18:42:21 2023

@author: Matthew Heino
"""

#import numpy as np
import pandas as pd
#from sklearn import linear_model
#import matplotlib.pyplot as plt
#from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
#from sklearn.metrics import confusion_matrix, accuracy_score
#from sklearn.model_selection import cross_val_score
from warnings import simplefilter


simplefilter(action='ignore', category=FutureWarning)

#  Load the data from the CSV file
iris_df = pd.read_excel('Week_06_HW6_Iris_Dataset.xlsx')
print(iris_df.head())

# get some dataabout the file
print(iris_df.info())

# Drop the Sample numbe ID from the frame
iris_df.drop(['sampleNum'], axis=1, inplace=True)
print(iris_df.head()) 

# see if there is a correation
print(iris_df.corr())

#Tried a different way
#feature_columns = ['sepalWidth', 'petalWidth']
feature_columns = ['sepalWidth']
#feature_columns = ['petalWidth']
X_ind =iris_df[feature_columns].values
Y_dep = iris_df['irisSpecies'].values 

# Encode the target column with a numeric value corresponding to the species 
# of the iris. 
lab_enc = LabelEncoder()
Y_dep = lab_enc.fit_transform(Y_dep)


# Create the test and training sets.
X_train, X_test, Y_train, Y_test = train_test_split(X_ind, Y_dep
                                                    , test_size = 0.50
                                                    , random_state=42)


# Creata the KNN model
# Instantiate learning model (k = 3)
knn_class = KNeighborsClassifier(n_neighbors=5)


# Fitting the model
knn_class.fit(X_train, Y_train)

# Predicting the Test set results
y_pred = knn_class.predict(X_test)

#Create a confusion matrix
con_matrix = confusion_matrix(Y_test, y_pred)
con_matrix

# see the Accruarcy score of the model
print("\nAccuracy: ", knn_class.score(X_test, Y_test))
print("R Squared", knn_class.score(X_test, Y_test) *100)



















