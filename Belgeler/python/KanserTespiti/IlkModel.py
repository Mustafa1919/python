from keras.models import Sequential
from keras.layers import Dense , Dropout , Activation
import keras
from keras.layers import Input , Dense
import keras.optimizers

from sklearn.preprocessing import Imputer
import numpy as np
import pandas as pd

veri = pd.read_csv("breast-cancer-wisconsin.data")

veri.replace('?',-999999,inplace=True)
veriYeni = veri.drop(['1000025'],axis=1)

imp = Imputer (missing_values=-99999,strategy="mean",axis=0)
veriYeni = imp.fit_transform(veriYeni)

giris = veriYeni[:,0:8]
cikis = veriYeni[:,9]

model = Sequential()
model.add(Dense(256,input_dim=8))
model.add(Activation('relu')) #relu sigmoid gibi bir fonksiyon node larda hesaplama yapıyor tanh da seçilebilir
model.add(Dropout(0.5))
model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(256))
model.add(Activation('softmax')) #sonuncu kesinlikle softmax olmalı

optimizer=keras.optimizers.rmsprop(lr=0.01)

model.compile(optimizer=optimizer,loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(giris,cikis,epochs=50,batch_size=32,validation_split=0.13)

tahmin = np.array([7,3,2,10,5,10,5,4]).reshape(1,8)
print("Tahmin1= {}".format(model.predict_classes(tahmin)))

tahmin = np.array([5,3,2,1,3,1,1,1]).reshape(1,8)
print("Tahmin2= {}".format(model.predict_classes(tahmin)))

tahmin = np.array([5,10,10,10,4,10,5,6]).reshape(1,8)
print("Tahmin3 = {}".format(model.predict_classes(tahmin)))