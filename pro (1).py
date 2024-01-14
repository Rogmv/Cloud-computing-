import numpy as np
import pandas as pd
import tensorflow as tf
import pickle
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from keras.models import Sequential
from sklearn.ensemble import RandomForestClassifier
from keras.layers import Conv2D,Activation,MaxPooling2D,Flatten,Dense,Dropout,BatchNormalization

da=pd.read_csv("Covid Dataset.csv")
#print(da.info())
da.drop('Running Nose',axis='columns',inplace=True)
da.drop('Asthma',axis='columns',inplace=True)
da.drop('Chronic Lung Disease',axis='columns',inplace=True)
da.drop('Heart Disease',axis='columns',inplace=True)
da.drop('Diabetes',axis='columns',inplace=True)
da.drop('Hyper Tension',axis='columns',inplace=True)
da.drop('Family working in Public Exposed Places',axis='columns',inplace=True)
da.drop('Wearing Masks',axis='columns',inplace=True)
da.drop('Sanitization from Market',axis='columns',inplace=True)
da.replace({'Yes':1,'No':0},inplace=True)
ip=da.drop("COVID-19",axis=1)
op=da["COVID-19"]
'''print(da.info())
print(ip.sample(2), op.sample(2))
print(op.value_counts())'''
ip_columns = ip.columns
train_x,test_x,train_y,test_y=train_test_split(ip,op,test_size=0.2,stratify=op)
model=Sequential()

model.add(Dense(units=11,activation='relu'))
model.add(Dense(units=12,activation='relu'))
model.add(Dense(units=6,activation='relu'))
model.add(Dense(units=1,activation='sigmoid'))
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
model.fit(train_x,train_y,epochs=10)
loss,accuracy=model.evaluate(test_x,test_y)
print(loss,accuracy)
f=open('model.p','wb')
pickle.dump({'model':model},f)
f.close()
