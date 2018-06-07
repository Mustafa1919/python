import os
import numpy as np
import keras
from keras.layers import Dense,Activation,Flatten,Dropout,Conv2D,MaxPool2D
from keras.models import Sequential
from keras.layers.convolutional import Convolution2D,MaxPooling2D
from keras.optimizers import SGD
from keras.layers.normalization import BatchNormalization
import ResimIsle
import matplotlib.pyplot as plt

if os.path.isfile("keras_egitim_verisi.npy") and os.path.isfile("keras_test_verisi.npy"):
    egitim_verisi = np.load("keras_egitim_verisi.npy")
    test_verisi = np.load("keras_test_verisi.npy")
else:
    ResimIsle.egitim_verisi_olustur("keras")
    ResimIsle.test_verisi_olustur("keras")
    egitim_verisi = np.load("keras_egitim_verisi.npy")
    test_verisi = np.load("keras_test_verisi.npy")    

x_egitim = np.array([i[0] for i in egitim_verisi]).reshape(-1,224,224,1) #eğitim setinden resimleri aldık
y_egitim = np.array([i[1] for i in egitim_verisi]) #eğitim setinden etiketleri aldık bunlar sonuc
x_test = np.array([i[0] for i in test_verisi]).reshape(-1,224,224,1)
y_test = np.array([i[1] for i in test_verisi])

model = Sequential()
model.add(Conv2D(96,11,strides=(4,4),input_shape=(224,224,1)))
model.add(MaxPooling2D(5,5))
model.add(Conv2D(256,5))
model.add(Conv2D(384,3))
model.add(Conv2D(384,3))
model.add(Conv2D(256,1))
model.add(Flatten())
model.add(Dense(4096,activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(4096,activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(3,activation="softmax"))
model.compile(loss="binary_crossentropy",optimizer=keras.optimizers.RMSprop(lr=0.0001),metrics=["accuracy"])
model.summary()
model.fit(x_egitim,y_egitim,batch_size=2,epochs=10,validation_split=0.3)

fig = plt.figure(figsize=(16,12))
for no , veri in enumerate(test_verisi):
    resim_no = veri[1]
    resim_verisi = veri[0]
    y=fig.add_subplot(4,4,no+1)
    orig = resim_verisi
    veri = resim_verisi.reshape(-1,224,224,1)
    ag_cikisi = model.predict([veri])
    print(ag_cikisi)
    if np.argmax(ag_cikisi) == 2:
        str_label = "sandalye"
    elif np.argmax(ag_cikisi) == 1:
        str_label = "masa"
    elif np.argmax(ag_cikisi) == 0:
        str_label = "koltuk"
    else:
        str_label = "Hata Olustu"
    
    y.imshow(orig,cmap="gray")
    plt.title(str_label)
    y.axes.get_xaxis().set_visible(False)
    y.axes.get_yaxis().set_visible(False)
plt.show()
