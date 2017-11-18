#-*-encoding=utf-8-*-

import random
import haritaSuper
import karakterSuper
import kiyafetlerSuper
import aksionSuper
import sys
new_harita=haritaSuper.HaritaSuper()
ana_karakter=karakterSuper.AnaKarakter()
action=aksionSuper.action()
dongu_degeri=0
def komutlar():
    print("{:<8} ----> Oyunu Başlatır\n".format("Basla")+
          "{:<8} ----> Zar Atar\n".format("Zar At")+
          "{:<8} ----> Haritayı Gösterir\n".format("Harita")+
          "{:<8} ----> Harita Özelliklerini Gösterir\n".format("Ozellik")+
          "{:<8} ----> Komut Listesini Sıralar\n".format("Komutlar")+
          "{:<8} ----> Oyunu Bitirir".format("Bitir"))
def zarAt():
    zar1=random.randint(1,6)
    zar2=random.randint(1,6)
    print("Atılan zarlar {} ve {}".format(zar1,zar2))
    return zar1+zar2

def oyunuBaslat():
    while ana_karakter.can > 0 :
        komut=input("Komut= ")
        if komut.lower() == "bitir":
            sys.exit()
        elif komut.lower() == "zar at":
            try:
                new_harita.konum += zarAt()
                print("Geldiğiniz nokta= {} konumu= {}".format(new_harita.harita[new_harita.konum],new_harita.konum))
                action.aksionKarsiligi(new_harita.harita[new_harita.konum],ana_karakter,new_harita)
                ##zar atıp konuma geldik gelen saldırıyı düzenleme kaldı 
                
                
            except IndexError as e:
                print("Tebrikler Oyunu Kazandınız ve Sonuna Kadar Geldiniz.")
                sys.exit()
    print("Malesef oyunu kaybettiniz.")
        
def dongu():
    global dongu_degeri
    if dongu_degeri == 0:
        dongu_degeri += 1
        oyunuBaslat()
    else :
        print("Zaten bir oyun içindesinizi önce oyununuzu bitiriniz.")
def komutGirisi(): 
    komut=input()
    if komut.lower() == "zar at":
        zarAt()
        komutGirisi()
    elif komut.lower() == "komutlar":
        komutlar()
        komutGirisi()
    elif komut.lower() == "harita":
        new_harita.haritaGoster()
        komutGirisi()
    elif komut.lower() == "ozellik":
        new_harita.haritaOzellikleri() 
        komutGirisi()
    elif komut.lower() == "basla":
        dongu()
    elif komut.lower() == "bitir":
        sys.exit()
    else :
        print("Hatalı bir giriş yaptınız lütfen komutları tekrar gözden geçirip komut giriniz.Türkçe karakter kullanmayınız.")
        komutGirisi()

print("Oyunumuza Hoşgeldiniz")
print("Lütfen komut girerken türkçe karakter kullanmayınız...")
print("Vermek istediğiniz komutu klavyeden yazınız. Örnek zar at gibi.")
komutlar()
komutGirisi()