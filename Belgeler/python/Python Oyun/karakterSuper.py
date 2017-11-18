#-*-encoding=utf-8-*-
import random

class Karakterler():
    def __init__(self):
        self.kasa=[]
        self.saldırıGucu=12
        self.savunmaGucu=15
        self.can=150
        self.adi="Ana Karakter"
        self.ustundekiler=[]
    def saldir(self,rakip):
        self.savasSimilasyonu(rakip)
    def savasSimilasyonu(self,rakip):
        print("Saldıran Adı={}\nSaldırılan Adı={}".format(self.adi,rakip.adi))
        print("Saldırı Gücü = {}\nSavunma Gücü = {}\nCan = {}".format(rakip.saldırıGucu,rakip.savunmaGucu,rakip.can))
        sayac=0
        while self.can>0 and rakip.can>0:
            if sayac % 2 == 0:
                saldiran_saldiri_puani = (int)((self.saldırıGucu/random.randint(1,6))-(rakip.savunmaGucu/random.randint(5,11)))
                if saldiran_saldiri_puani < 0:
                    pass
                else:
                    rakip.can -= saldiran_saldiri_puani
                sayac+=1
            else :
                saldiri_puani= (int)((rakip.saldırıGucu/random.randint(3,7))-(self.savunmaGucu/random.randint(5,9)))
                #print("saldırı puanı = {}  kalan can = {}".format(saldiri_puani,self.can))
                if saldiri_puani < 0:
                    pass
                else:
                    self.can -= saldiri_puani
                sayac+=1
        
class AnaKarakter(Karakterler):
    def __init__(self):
        super().__init__()
    def kıyafetGiy(self,kiyafet,oyuncu):
        if len(self.kasa) == 0:
            print("Kasanız boş kıyafet giyemezsiniz.")
        else :
            kiyafet.kiyafetGiy(oyuncu)
            
    def kiyafetListele(self):
        if len(self.ustundekiler) == 0:
            print("Üstünüzde kıyafet yok")
        else:
            for i in self.ustundekiler:
                print("{:>20}".format(i))
    def kasaListele(self):
        if len(self.kasa) == 0:
            print("Kasanızda kıyafet yok.")
        else:
            for i in self.kasa:
                print("{:>20}".format(i))
    def ozellikGoster(self):
        print("Saldırı Gücü = {}\nSavunma Gücü = {}\nCan = {}".format(self.saldırıGucu,self.savunmaGucu,self.can))
class Yeniceri(Karakterler):
    def __init__(self):
        self.saldırıGucu=10
        self.can=20
        self.savunmaGucu=10
        self.adi="Yeniçeri"

class Baltali(Karakterler):
    def __init__(self):
        self.can=35
        self.saldırıGucu=5
        self.savunmaGucu=10
        self.adi="Baltalı"

class Atli(Karakterler):
    def __init__(self):
        self.can=25
        self.saldırıGucu=13
        self.savunmaGucu=15
        self.adi="Atlı"

class Mızraklı(Karakterler):
    def __init__(self):
        self.can=30
        self.savunmaGucu=15
        self.saldırıGucu=7
        self.adi="Mızraklı"
