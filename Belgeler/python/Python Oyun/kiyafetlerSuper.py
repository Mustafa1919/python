#-*-encoding=utf-8-*-


class Kiyafetler():
    def __init__(self):
        self.adi="Mızrak"
        self.ozellik="+8 Atak Gücü"
    def ozellikGoster(self):
        print("{} adlı eşyanın özelliği {}".format(self.adi,self.ozellik))
    def kiyafetGiy(self,oyuncu):
        oyuncu.saldırıGucu += 8
        oyuncu.ustundekiler.append(self.adi)
    def kiyafetCikar(self,oyuncu):
        oyuncu.saldırıGucu -= 8
        oyuncu.ustundekiler.remove(self.adi)
    def mesaj(self):
        print("Tebrikler {} kıyafetini kazandınız.".format(self.adi))
        
class Hancer(Kiyafetler):
    def __init__(self):
        self.adi="Hançer"
        self.ozellik="+3 Atak Gücü"
    def kiyafetGiy(self,oyuncu):
        oyuncu.saldırıGucu += 3
        oyuncu.ustundekiler.append(self.adi)
    def kiyafetCikar(self,oyuncu):
        oyuncu.saldırıGucu -=3
        oyuncu.ustundekiler.remove(self.adi)
        
class Kilic(Kiyafetler):
    def __init__(self):
        self.adi="Kılıç"
        self.ozellik="+5 Atak Gücü"
    def kiyafetGiy(self,oyuncu):
        oyuncu.saldırıGucu +=5
        oyuncu.ustundekiler.append(self.adi)
    def kiyafetCikar(self,oyuncu):
        oyuncu.saldırıGucu -=5
        oyuncu.ustundekiler.remove(self.adi)
        
class Mizrak(Kiyafetler):
    def __init__(self):
        super().__init__()

class KumasElbise(Kiyafetler):
    def __init__(self):
        self.adi="Kumaş Elbise"
        self.ozellik="+20 Can"
    def kiyafetGiy(self,oyuncu):
        oyuncu.can += 20
        oyuncu.ustundekiler.append(self.adi)
    def kiyafetCikar(self,oyuncu):
        oyuncu.cn -= 20
        oyuncu.ustundekiler.remove(self.adi)

class TahtaKalkan(Kiyafetler):
    def __init__(self):
        self.adi="Tahta Kalkan"
        self.ozellik="+5 Defans Gücü"
    def kiyafetGiy(self,oyuncu):
        oyuncu.savunmaGucu += 5
        oyuncu.ustundekiler.append(self.adi)
    def kiyafetCikar(self,oyuncu):
        oyuncu.savunmaGucu -= 5
        oyuncu.ustundekiler.remove(self.adi)
    
class Migfer(Kiyafetler):
    def __init__(self):
        self.adi="Miğfer"
        self.ozellik="+5 Savunma Gücü"
    def kiyafetGiy(self,oyuncu):
        oyuncu.savunmaGucu += 5
        oyuncu.ustundekiler.append(self.adi)
    def kiyafetCikar(self,oyuncu):
        oyuncu.savunmaGucu -= 5
        oyuncu.ustundekiler.remove(self.adi)
        
class Bileklik(Kiyafetler):
    def __init__(self):
        self.adi="Bileklik"
        self.ozellik="+5 Can"
    def kiyafetGiy(self,oyuncu):
        oyuncu.can += 5
        oyuncu.ustundekiler.append(self.adi)
    def kiyafetCikar(self,oyuncu):
        oyuncu.can -= 5
        oyuncu.ustundekiler.remove(self.adi)

class Ayakkabi(Kiyafetler):
    def __init__(self):
        self.adi="Ayakkabı"
        self.ozellik="+15 Can"
    def kiyafetGiy(self,oyuncu):
        oyuncu.can += 15
        oyuncu.ustundekiler.append(self.adi)
    def kiyafetCikar(self,oyuncu):
        oyuncu.can -= 15
        oyuncu.ustundekiler.remove(self.adi)
        
class Kalkan(Kiyafetler):
    def __init__(self):
        self.adi="Kalkan"
        self.ozellik="+10 Savunma Gücü"
    def kiyafetGiy(self,oyuncu):
        oyuncu.savunmaGucu += 10
        oyuncu.ustundekiler.append(self.adi)
    def kiyafetCikar(self,oyuncu):
        oyuncu.savunmaGucu -= 10
        oyuncu.ustundekiler.remove(self.adi)
        
class Bonus(Kiyafetler):
    def __init__(self):
        self.adi="At"
        self.ozellik="+20 Savunma Gucu"
    def kiyafetGiy(self,oyuncu):
        oyuncu.savunmaGucu += 20
    def kiyafetCikar(self,oyuncu):
        oyuncu.savunmaGucu -=20
    def mesaj(self):
        print("Tebrikler Bonus Ödülü Kazandınız")
        super().mesaj()
        
        
