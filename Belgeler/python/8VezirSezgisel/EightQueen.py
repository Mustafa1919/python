import numpy as np
import random

class EightQueen():

    def __init__(self):
        self.tahta=np.zeros((8,8))
        self.degerAta()

    def degerAta(self):
        for i in range(8):
            self.tahta[i][random.randint(0,7)]=1

    def eightQueen(self):
        sezgiselDegerler=self.sezgiselHesapla()
        dongu = 0
        while dongu < 30:
            if np.sum(sezgiselDegerler) == 0 :
                break
            else:
                enBuyuk=np.max(sezgiselDegerler)
                konum=sezgiselDegerler.index(enBuyuk)
                y=self.konumBul(konum)
                ##self.tahta[konum][y] = 0
                self.hamleYap(konum,y)
                print(self.tahta)
                ##print("\n")
                ##test=input()
                sezgiselDegerler=self.sezgiselHesapla()
                ##print(sezgiselDegerler)
                ##print("Tahta")
            dongu += 1
            if dongu == 30:
                print("Geçerli bir çözüm malesef bulunamadı")


    def sezgiselHesapla(self):
        sezgiselListe=[]
        for i in range(8):
            adet=0
            y=self.konumBul(i)
            for j in range(8):
                if j==i:
                    pass
                else:
                    if self.tahta[j][y]==1:
                        adet += 1
            kopyaX,kopyaY,testX,testY=i-1,y-1,i+1,y+1
            while kopyaX >=0 or kopyaY >=0 or testX <= 7 or testY <= 7:
                if kopyaX >= 0 and kopyaY >= 0:
                    if self.tahta[kopyaX][kopyaY] == 1:
                        adet += 1
                if kopyaX >= 0 and testY <= 7:
                    if self.tahta[kopyaX][testY] == 1:
                        adet += 1
                if testX <= 7 and kopyaY >= 0:
                    if self.tahta[testX][kopyaY] == 1:
                        adet += 1
                if testX <= 7 and testY <= 7:
                    if self.tahta[testX][testY] == 1:
                        adet += 1
                kopyaX -= 1
                kopyaY -= 1
                testX += 1
                testY += 1
            sezgiselListe.append(adet)
        return sezgiselListe

    def konumBul(self,satir):
        for k in range(8):
            if self.tahta[satir][k] == 1:
                return k

    def hamleYap(self, konum, sıfırlanacak):
        hamle=[]
        for i in range(8):
            kontrol = True
            for j in range(8):
                if self.tahta[j][i] == 1:
                    kontrol = False
                    break
            if kontrol :
                hamle.append(i)
        ##dikey koordinatları bulduk bu bulunan noktalardan en uygununu bulmak kaldı sağ ve sol taraması yapılacak
        if len(hamle) == 0:
            pass
        else:
            hamleSezgisel=[]
            for i in range(len(hamle)):
                adet=0
                kopyaX, kopyaY, testX, testY = konum - 1, hamle[i] - 1, konum + 1, hamle[i] + 1
                while kopyaX >= 0 or kopyaY >= 0 or testX <= 7 or testY <= 7:
                    if kopyaX >= 0 and kopyaY >= 0:
                        if self.tahta[kopyaX][kopyaY] == 1:
                            adet += 1
                    if kopyaX >= 0 and testY <= 7:
                        if self.tahta[kopyaX][testY] == 1:
                            adet += 1
                    if testX <= 7 and kopyaY >= 0:
                        if self.tahta[testX][kopyaY] == 1:
                            adet += 1
                    if testX <= 7 and testY <= 7:
                        if self.tahta[testX][testY] == 1:
                            adet += 1
                    kopyaX -= 1
                    kopyaY -= 1
                    testX += 1
                    testY += 1
                hamleSezgisel.append(adet)
            enKucuk=np.min(hamleSezgisel)
            hamleKonum=hamleSezgisel.index(enKucuk)
            self.tahta[konum][sıfırlanacak] = 0
            self.tahta[konum][hamle[hamleKonum]] = 1


deneme=EightQueen()
deneme.eightQueen()