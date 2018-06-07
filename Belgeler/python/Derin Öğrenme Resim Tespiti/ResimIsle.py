import cv2
import numpy as np
from tqdm import tqdm
import os
from random import shuffle

def etiket_olustur(resimAdi):
    objeTuru = resimAdi.lower().split(".")[0]
    if  objeTuru[0] == "k":
        return np.array([1,0,0])
    elif objeTuru[0] == "m":
        return np.array([0,1,0])
    elif objeTuru[0] == "s":
        return np.array([0,0,1])
    else:
        print("Hatalı Giriş")

def egitim_verisi_olustur(tip):
    olusturulanEgitimVerisi=[]
    for img in tqdm(os.listdir("Train")):
        dosyaYolu = os.path.join("Train",img) #dosyanın path yolunu döndürüyor
        resimVerisi = cv2.imread(dosyaYolu,cv2.IMREAD_GRAYSCALE)
        if tip.lower() == "keras":
            resimVerisi = cv2.resize(resimVerisi,(224,224))
        else:
            resimVerisi = cv2.resize(resimVerisi,(50,50))
        olusturulanEgitimVerisi.append([np.array(resimVerisi),etiket_olustur(img)])
    shuffle(olusturulanEgitimVerisi)
    if tip.lower() == "keras":
        np.save("keras_egitim_verisi.npy",olusturulanEgitimVerisi)
    else:
        np.save("egitim_verisi.npy",olusturulanEgitimVerisi)

def test_verisi_olustur(tip):
    olusturulan_test_verisi = []
    sira_no = 1
    for img in tqdm(os.listdir("Test")):
        dosyaYolu = os.path.join("Test",img)
        resimVerisi = cv2.imread(dosyaYolu,cv2.IMREAD_GRAYSCALE)
        if tip.lower() == "keras":
            resimVerisi = cv2.resize(resimVerisi,(224,224))
        else:        
            resimVerisi = cv2.resize(resimVerisi,(50,50))
        olusturulan_test_verisi.append([np.array(resimVerisi),sira_no])
        sira_no += 1
    shuffle(olusturulan_test_verisi)
    if tip.lower() == "keras":
        np.save("keras_test_verisi.npy",olusturulan_test_verisi)  
    else:
        np.save("test_verisi.npy",olusturulan_test_verisi)


