import pandas as pd
import numpy as np
from sklearn.preprocessing import  normalize
from keras.models import Sequential
from keras.layers import Dense,Activation,Dropout
#from tensorflow.keras.layers import BatchNormalization
from keras.utils import np_utils
from warnings import simplefilter

simplefilter(action='ignore', category=FutureWarning)


#  Load the data from the CSV file
iris_df = pd.read_excel('Week_06_HW6_Iris_Dataset.xlsx')
#print(iris_df.head())

# get some data about the file
print(iris_df.info())

# Drop the Sample numbe ID from the frame
iris_df.drop(['sampleNum'], axis=1, inplace=True)
#print(iris_df.head())


# Replace species category with a number.
iris_df['irisSpecies'].replace(['Iris-setosa','Iris-versicolor'], [1,0], inplace=True)
print("\nAfter REPLACEMENT***********************")
print(iris_df)

#see if there is a correation
print(iris_df.corr())


#Tried a different ways
feature_columns = ['sepalWidth', 'petalWidth']
#feature_columns = ['sepalWidth']
#feature_columns = ['petalWidth']
X_ind =iris_df[feature_columns].values
Y_dep = iris_df['irisSpecies'].values
#print("Shape of X: ", X_ind.shape)
#print("Shape of Y: ", Y_dep.shape)

#Try a little data normalization of the data.
X_normalized=normalize(X_ind,axis=0)
print("Examples of X_normalised\n", X_normalized[:3])

# create the training, test and the validation datasets.
# A different way of doing things.

tot_len = len(iris_df)
train_len = int(0.8*tot_len)
test_len = int(0.2*tot_len)

"""
print("\nTotal length: ", tot_len)
print("Train length: ", train_len)
print("Test length: ", test_len)
"""



#Create the X training and X test sets.
X_train = X_normalized[ :train_len]
X_test = X_normalized[train_len: ]
#print("\nX train length: ", len(X_train))
#print("X test length: ", len(X_test))



#Create the Y training and Y test sets.
Y_train = Y_dep[ :train_len]
Y_test = Y_dep[train_len: ]
#print("\nY train length: ", len(Y_train))
#print("Y test length: ", len(Y_test))




#Change the label of the target array from string to integer
#print("\n\n", Y_train)
#print("\n\n", Y_test)
Y_train = np_utils.to_categorical(Y_train, num_classes=3)
Y_test = np_utils.to_categorical(Y_test, num_classes=3)

#print("Shape of Y Train: ", Y_train.shape)
#print("Shape of Y Test: ", Y_test.shape)

# Create a sequential model
seq_model=Sequential()
seq_model.add(Dense(1000, input_dim=2, activation='relu'))
seq_model.add(Dense(500, activation='relu'))
seq_model.add(Dense(300, activation='relu'))
seq_model.add(Dropout(0.2))
seq_model.add(Dense(3, activation='softmax'))
seq_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

print(seq_model.summary())


seq_model.fit(X_train, Y_train, validation_data=(X_test, Y_test), batch_size=10, epochs=5, verbose=1)

prediction = seq_model.predict(X_test)
length = len(prediction)
y_label = np.argmax(Y_test, axis=1)
predict_label = np.argmax(prediction, axis=1)

accuracy=np.sum(y_label == predict_label)/length * 100
print("Accuracy of the dataset", accuracy)
