import ResimIsle
import numpy as np
import tensorflow as tf
import tflearn
from tflearn.layers.conv import conv_2d,max_pool_2d
from tflearn.layers.core import input_data,dropout,fully_connected
from tflearn.layers.estimator import regression
import os
import matplotlib.pyplot as plt

if os.path.isfile("egitim_verisi.npy") and os.path.isfile("test_verisi.npy"):
    egitim_verisi = np.load("egitim_verisi.npy")
    test_verisi = np.load("test_verisi.npy")
else:
    ResimIsle.egitim_verisi_olustur("tenserflow")
    ResimIsle.test_verisi_olustur("tenserflow")
    egitim_verisi = np.load("egitim_verisi.npy")
    test_verisi = np.load("test_verisi.npy")    
egitim = egitim_verisi[:123]
test = egitim[-30:]

x_egitim = np.array([i[0] for i in egitim]).reshape(-1,50,50,1) #eğitim setinden resimleri aldık
y_egitim = [i[1] for i in egitim] #eğitim setinden etiketleri aldık bunlar sonuc
x_test = np.array([i[0] for i in test]).reshape(-1,50,50,1)
y_test = [i[1] for i in test]

#mimarinin oluşturulması 
tf.reset_default_graph()

convet = input_data(shape=[None , 50 , 50 , 1],name="input")
convet = conv_2d(convet , 32 , 5 , activation="relu") #32 tane 5x5 lik filtre
convet = max_pool_2d(convet , 5)
convet = conv_2d(convet , 64 , 5 , activation="relu")
convet = max_pool_2d(convet , 5)
convet = conv_2d(convet,128,5,activation="relu")
convet = max_pool_2d(convet,5)
convet = conv_2d(convet , 64 , 5 , activation="relu")
convet = max_pool_2d(convet,5)
convet = conv_2d(convet , 32 , 5 ,activation="relu")
convet = max_pool_2d(convet,5)

#1024 birimden oluşan tam bağlantılı katman 
convet = fully_connected(convet,1024,activation="relu")
convet = dropout(convet,0.8)
#3 birimli tam bağlantılı çıkış katmanı
convet =fully_connected(convet,3,activation="softmax")
convet = regression(convet,optimizer="adam",learning_rate=0.001,loss="categorical_crossentropy",name="targets")
#oluşturulan mimari ile deep learning network modeli oluşturulması 
model = tflearn.DNN(convet,tensorboard_dir="log",tensorboard_verbose=0)

#verilerin eğitim yapılması
model.fit({"input":x_egitim},{"targets":y_egitim},n_epoch=10,
          validation_set=({"input":x_test},{"targets":y_test}),
          snapshot_step=500,show_metric=True,run_id="Koltuk Sandalye Masa Tahmin")

#oluşturulan ağ modelinin test klasöründeki veriler üzerinde denenmesi
fig = plt.figure(figsize=(16,12))
for no , veri in enumerate(test_verisi):
    resim_no = veri[1]
    resim_verisi = veri[0]
    y=fig.add_subplot(4,4,no+1)
    orig = resim_verisi
    veri = resim_verisi.reshape(50,50,1)
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