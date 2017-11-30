#-*-encoding=utf-8-*-
import random
import numpy as np
import copy
import BreadthDepth

agac=[]
#bu fonksiyonlar arama uzayı oluşturulacak
def searchTree(liste):       
    if liste[0][1] >= 6:
        pass    #liste boş eleman veya son satıra gelince pass geçiyoruz
    else:
        sayisi=1
        test=[] #yeniden döndürülecek boş liste
        for i in liste: #liste elemanlarını çıkarıyoruz
            for j in range(8):  #ilgili satırda bakıyoruz
                if markOne(i[0],i[1]+2,j): #hamle yapılabiliyorsa
                    testTahta=copy.deepcopy(i[0]) #üzerinde işlem yapmak için tahtayı kopyalıyoruz
                    testTahta[i[1]+2][j]=1 #hamleyi yapıyoruz
                    test.append([testTahta,i[1]+1,sayisi]) #geri döndürmek için test dizisine ekliyoruz
            sayisi += 1
        agac.append(test)
        if len(test) != 0:
            print("Dizi boyutu={} Dizi parenti={}".format(len(test),test[0][1]))
        searchTree(test)
    
    
    
    #gönderilen noktanın hamle için uygun olup olmadığı test edildi 
def markOne(tahta,locationX,locationY):
    testX,testY,denemeY=locationX-1,locationY-1,locationY+1
    for i in range(locationX):
        if tahta[i][locationY]==1:
            return False
    while testX>=0 or testY>0 or denemeY<=7:
        if testX>=0 and testY>=0:
            if tahta[testX][testY]==1:
                return False
        if denemeY<=7 and testX>=0:
            if tahta[testX][denemeY]==1:
                return False
        testX -= 1
        testY -=1
        denemeY += 1
    return True

luckly=random.randint(0,7) #8 veziri aramaya başlanacak ilk nokta seçildi
board=np.zeros((8,8),dtype=np.int16) # 8x8 e zero matris oluşturuldu
board[0][luckly]=1 #ilk vezir yerleştirildi
first=[[board,-1,0]] #listeye root düğümü ekledik
searchTree(first) #ağacı oluşturmak için gönderdik  
bre=BreadthDepth.Depth()
#bre.breadth(agac)
bre.depth(agac)

             
        

