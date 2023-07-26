# -*- coding: utf-8 -*-
"""
Created on Mon May 22 06:17:41 2023

@author: Matthew Heino

https://regenerativetoday.com/complete-detailed-tutorial-on-linear-regression-in-python/
"""

import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
#import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm 
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

X_var = iris_df.petalWidth.values
#print("Petal width: \n", X_var)

Y_var = iris_df.irisSpecies.values
#print("Iris Species: \n", Y_var)


#Scatter plot of X and Y values
"""
plt.scatter(X_var, Y_var, color='blue')
plt.xlabel("Petal Width")
plt.ylabel("Iris Species")
plt.plot()
"""

X_var = X_var.reshape(-1,1)
 
x_train, x_test, y_train, y_test = train_test_split(X_var,Y_var,train_size=0.80
                                                    , random_state=42)

#print(x_train, len(x_train))
#print(x_test, len(x_test))


#Scatter plot of X and Y values
plt.scatter(x_train, y_train, color='blue')
plt.xlabel("Petal Width Training Set")
plt.ylabel("Iris Species Training Set")
plt.plot()

# Create the linear regression
lin_reg = LinearRegression()

lin_reg.fit(x_train, y_train)

#Calcualte the score
r_sq = lin_reg.score(x_train , y_train) * 100
print("R-squared score: ", r_sq)

#Predict some values
y_predict = lin_reg.predict(x_test)
#prediced Values
print(y_predict)

plt.scatter(x_train, y_train, color='blue')
plt.scatter(x_test, y_predict, color='green')
plt.xlabel("Petal Width")
plt.ylabel("Iris Species")
plt.plot()




# multivariate
x_ind = iris_df[['sepalWidth','petalWidth']].values.reshape(-1,2)
y_dep = iris_df['irisSpecies']


# Create tje model.
lin_reg = linear_model.LinearRegression()
lin_reg.fit(x_ind, y_dep)
 
print('Intercept: \n', lin_reg.intercept_)
print('Coefficients: \n', lin_reg.coef_)
print("R Squared", lin_reg.score(x_ind, y_dep) *100)

x_ind = sm.add_constant(x_ind) # adding a constant

model = sm.OLS(y_dep, x_ind).fit()
predictions = model.predict(x_ind) 
 
print_model = model.summary()
print(print_model)










