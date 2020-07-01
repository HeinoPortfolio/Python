# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:19:28 2019

@author: Admin
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import requests as req
import json as jsn
import re
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics



pd.set_option('display.max_columns', None)
pd.set_option('display.max_columns', None)

filepath_titanic = 'titanic3.csv'

#Read the data into a dataframe
titanic_frame = pd.read_csv(filepath_titanic, sep=',')

# Print part of the frame.

#print (titanic_frame.shape)
#print (titanic_frame.head(5))

#List the columns for the frame
#print (list(titanic_frame.columns))

# Change the column the column destination
#split the home and destination into two separate columns
home_dest_frame = titanic_frame['home.dest'].str.split("/", n = 1, expand = True) 

#print (home_dest_frame.head())
#print (home_dest_frame.tail())

#Add these columns to the frame
titanic_frame['Home'] = home_dest_frame[0]
titanic_frame['Destination'] = home_dest_frame[1]
#drop the unneeded column
titanic_frame.drop(columns = ['home.dest'], inplace = True)

#print the frame with the new columns added.
#print (titanic_frame.head())

"""
#Find out how many women and men. How many men and women are there on the list
men_women = titanic_frame.groupby('sex').size()
print (men_women)

#Show a graph of the passenges based on sex

print(men_women.plot.bar())
men_women = men_women.plot.bar().get_figure()

men_women.savefig("Men and Women.png")




print (len(titanic_frame))
"""


#How many were in each of the different classes?

"""
men_women_class = titanic_frame.groupby(['pclass','sex'])['sex'].agg(np.size)

print(men_women_class)


men_women_class = titanic_frame.groupby(['pclass','sex'])['sex'].agg(np.size)

print (men_women_class.unstack().plot.bar())
men_women_class = men_women_class.unstack().plot.bar().get_figure()
men_women_class.savefig("Men and Women by Class.png")
"""

#Average age of a Titanic Passnege

#print(titanic_frame.groupby('sex').age.mean())  

#Average age by class
#print(titanic_frame.groupby('pclass').age.mean())  



#name = name.split(',')
#print (len(name))
#print (name)

"""
last_name = name[0][7:]
first_name = name[1].split("\n")[0].strip()
"""

"""
last_name = re.split('[0-9]+', name[0])[1].strip()
first_name = name[1].split("\n")[0].strip()

print (last_name)
print (first_name)
"""

#Rebuild the name
#full_name = first_name + " " + last_name

#print (full_name)

# Look for article

pd.set_option('display.max_columns', None)
#pd.set_option('display.max_colwidth', 30)
pd.set_option('display.width', 2000)

#youngest = full_name

def find_articles(name):
    
    url = ("https://api.nytimes.com/svc/search/v2/articlesearch.json?q="+name+"&begin_date=19120301&end_date=19120630&api-key=Xfga4BEJz505L3gPiEaxroTrACqCfDDy")
    result = req.get(url)
    articles = result.json()
    
    print (type(articles))
    print (len(articles))
    print (len(articles['response']['docs']))
    if len(articles['response']['docs']) != 0:
        print (articles['response']['docs'][0].keys())
        web_url_lst = []
        snippet_lst = []
        headline_lst = []
        byline_lst = []
        for x in articles['response']['docs']:
            web_url_lst.append(x['web_url'])
            snippet_lst.append(x['snippet'])
            headline_lst.append(x['headline']['main'])
            byline_lst.append(x['byline']['original']) 
            
        #add the frame code goes here
        print (web_url_lst)
        # create the dataframe
        data_dict = {'Web URL': web_url_lst, 'Snippet': snippet_lst,
             'Headline': headline_lst,  'Byline': byline_lst}
        article_frame = pd.DataFrame(data_dict)
        print (article_frame)
    else:
        print ("No articles found!")        

def extract_name(name):
    
    name = name.split(',')
    last_name = re.split('[0-9]+', name[0])[1].strip()
    first_name = name[1].split("\n")[0].strip()
    #Rebuild the name
    full_name = first_name + " " + last_name
    
    return full_name


#Finding the youngest passenger on the Titanic
    

"""
youngest_passenger = titanic_frame[titanic_frame.age == titanic_frame.age.min()]
print (youngest_passenger[['pclass', 'name', 'age']])

oldest_passenger = titanic_frame[titanic_frame.age == titanic_frame.age.max()]
print (oldest_passenger[['pclass', 'name', 'age']])


# fiding information about the Titanic passengers.
print ("\n \n")
print (youngest_passenger['name'])

young_name = str(youngest_passenger['name'])
old_name = str(oldest_passenger['name'])

print ("\n\nExtracted")
print (extract_name(young_name))
print (extract_name(old_name))


#FInd articels for the youngest passenger
find_articles(young_name)
find_articles(old_name)
find_articles("John Jacob Astor")


#Find the total count of survivors grouped by sex.
#List the columns for the frame
#print (list(titanic_frame.columns))
"""

titanic_frame_calc = titanic_frame[['pclass', 'survived', 'sex','age']]

#print(titanic_frame_calc.head(20))

titanic_frame_calc['survived'] = titanic_frame_calc['survived'].map({1: 'Yes', 0: 'No'})

"""
print(titanic_frame_calc.head(20))

men_women_survive = titanic_frame_calc.groupby('survived').size()
print (men_women_survive)
print(men_women_survive.plot.bar())
men_women_survive = men_women_survive.plot.bar().get_figure()
men_women_survive.savefig("Men and Women Survive.png")
"""
"""
#find the average age

titanic_frame_calc['pclass'] = titanic_frame_calc['pclass'].map({1: 'First', 2: 'Second', 3: 'Third'})

#print(titanic_frame_calc.head())

print(titanic_frame_calc.groupby(['sex', 'pclass', 'survived']).age.mean())


#print(titanic_frame_calc.head(20))


#Create a bar graph.
#print (titanic_frame_calc.groupby(['sex', 'pclass', 'survived']).age.mean().unstack().plot.bar())
titanic_frame_calc = titanic_frame_calc.groupby(['sex', 'pclass', 'survived']).age.mean().unstack().plot.bar()
#print(type(survive))
survive = titanic_frame_calc.get_figure()
survive.savefig("Men and Women Survive Mean.png")


"""
# make predictions about the Titanic
print(titanic_frame_calc.shape)
print (titanic_frame_calc.columns)

lbl_enc = LabelEncoder()

for col in titanic_frame_calc.columns:
    print (col)
    #Encode the columns with numerics
    titanic_frame_calc[col] = lbl_enc.fit_transform(titanic_frame_calc[col])
    
print(type(titanic_frame_calc))
print(titanic_frame_calc.shape)
#print (titanic_frame_calc[150:500])
#print (titanic_frame_calc.

titanic_dummies_frame = pd.get_dummies(titanic_frame_calc)

feature_cols = ['survived','sex','age']

X = titanic_dummies_frame[feature_cols] 

# Create a subset of the Mush_dummies dataframe for respones
y = titanic_dummies_frame['pclass']

# Instantiate .
knn_titan = KNeighborsClassifier(n_neighbors=1)
knn_titan.fit(X, y)
test2 = knn_titan.predict(X)
print (metrics.accuracy_score(y, test2))

knn_titan = KNeighborsClassifier(n_neighbors=10)
knn_titan.fit(X, y)
test = knn_titan.predict(X)
print (metrics.accuracy_score(y, test))

#Using a logistic regression
logreg_titan = LogisticRegression()
logreg_titan.fit(X,y)

y_pred = logreg_titan.predict(X)

#Classification Accuracy
print (metrics.accuracy_score(y, y_pred))



# Using sex as a predictor
feature_cols = ['survived','pclass','age']

X = titanic_dummies_frame[feature_cols] 

# Create a subset of the Mush_dummies dataframe for respones
y = titanic_dummies_frame['sex']

# Instantiate .
knn_titan = KNeighborsClassifier(n_neighbors=1)
knn_titan.fit(X, y)
test2 = knn_titan.predict(X)
print (metrics.accuracy_score(y, test2))

knn_titan = KNeighborsClassifier(n_neighbors=10)
knn_titan.fit(X, y)
test = knn_titan.predict(X)
print (metrics.accuracy_score(y, test))

#Using a logistic regression
logreg_titan = LogisticRegression()
logreg_titan.fit(X,y)

y_pred = logreg_titan.predict(X)

#Classification Accuracy
print (metrics.accuracy_score(y, y_pred))

"""



#*****************************************

#Format the oldest passenger
#oldest_passenger = titanic_frame[titanic_frame.age == titanic_frame.age.max()]
#print (oldest_passenger[['pclass', 'name', 'age']])




# fiding information about the Titanic passengers.
print ("\n \n")
print (oldest_passenger['name'])

name = str(oldest_passenger['name'])

name = name.split(',')
print (len(name))
print (name)


#last_name = name[0][6:]
#first_name = name[1].split("\n")[0].strip()

name_splt = re.split('[0-9]+', name[0])
print(name[1])
name_splt

print(name_splt)



#print (last_name)
#print (first_name)

"""











