# -*- coding: utf-8 -*-
"""
Created on Tue May 23 03:49:55 2023

@author: ntcrw
"""

import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
#import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
#from sklearn.preprocessing import StandardScaler
#import statsmodels.api as sm 
#from statsmodels.stats.outliers_influence import variance_inflation_factor
#from mpl_toolkits.mplot3d import Axes3D

#  Load the data from the CSV file

iris_df = pd.read_excel('Week_06_HW6_Iris_Dataset.xlsx')
#print(iris_df)



# get some dataabout the file
print(iris_df.info())

# Drop the Sample numbe ID from the frame
iris_df.drop(['sampleNum'], axis=1, inplace=True)
#print(iris_df) 

# Replace species category with a number.
iris_df['irisSpecies'].replace(['Iris-setosa','Iris-versicolor'], [1,0], inplace=True) 
print("After REPLACEMENT***********************")
#print(iris_df)

# see if there is a correation
print(iris_df.corr())

# Create the X and y varailbes for the set
X_ind = iris_df.drop(columns = ['irisSpecies','petalWidth'])
print(X_ind, type(X_ind))
Y_dep = iris_df['irisSpecies']
print(Y_dep, type(Y_dep))

X_train, X_test, Y_train, Y_test = train_test_split(X_ind, Y_dep
                                                    , test_size = 0.50
                                                    ,random_state=42)

#Create the Model
log_reg = linear_model.LogisticRegression()

#train the model
log_reg.fit(X_train, Y_train)

# see the Accruarcy score of the model
print("\nAccuracy: ", log_reg.score(X_test, Y_test))


# Create some predictions
pred = log_reg.predict(X_test)

print("R Squared", log_reg.score(X_test, Y_test) *100)


plt.scatter(X_train, Y_train, color='blue')


plt.scatter(X_test, pred, color='green')
plt.xlabel("Petal Width")
plt.ylabel("Iris Species")
plt.plot()



acc = accuracy_score(Y_train, pred)
print(acc)
acc1 = accuracy_score(pred, Y_test) 
print(acc1)

#Confusion matrix
print(confusion_matrix(Y_test, pred))

#print classification report
print(classification_report(Y_test, pred))




