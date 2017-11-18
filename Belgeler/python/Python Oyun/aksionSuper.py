#-*-encoding=utf-8-*-
import haritaSuper
import kiyafetlerSuper
import karakterSuper
import random
import sys

aksionHarita=haritaSuper.HaritaSuper()
mizrakli=karakterSuper.Mızraklı()
atli=karakterSuper.Atli()
baltali=karakterSuper.Baltali()
yeniceri=karakterSuper.Yeniceri()
bonus=kiyafetlerSuper.Bonus()
hancer=kiyafetlerSuper.Hancer()
kumas_elbise=kiyafetlerSuper.KumasElbise()
bileklik=kiyafetlerSuper.Bileklik()
kilic=kiyafetlerSuper.Kilic()
tahta_kalkan=kiyafetlerSuper.TahtaKalkan()
ayakkabi=kiyafetlerSuper.Ayakkabi()
mizrak=kiyafetlerSuper.Mizrak()
migfer=kiyafetlerSuper.Migfer()
demir_kalkan=kiyafetlerSuper.Kalkan() 

class action():
    def __init__(self):
        pass
     
    def randomUret(self):
        giysiDerece=random.randint(0,9)
        if giysiDerece > 0 and giysiDerece < 7:
            return 1
        else:
            return 2
      
    def kiyafetKontrol(self,oyuncu,kiyafet):
        if kiyafet not in oyuncu.ustundekiler and kiyafet in oyuncu.kasa:
            return True
        else:
            return False
       
    def aksionKarsiligi(self,islem,oyuncu,new_harita):
        newOzellik=aksionHarita.haritaOzellik
        if islem == "Bonus":
            bonus.kiyafetGiy(oyuncu)
            bonus.mesaj()
            print("At Giyildi")
            oyuncu.ozellikGoster()
        elif islem == "Random Askeri Saldırı":
            sayi=random.randint(0,3)
            if sayi == 1:
                atli.saldir(oyuncu)
                print("Atlı saldırısına uğradınız.")
                oyuncu.ozellikGoster()
            elif sayi == 0:
                mizrakli.saldir(oyuncu)
                print("Mızraklı saldırısına uğradınız.")
                oyuncu.ozellikGoster()
            elif sayi == 2:
                yeniceri.saldir(oyuncu)
                print("Yeniçeri saldırısına uğradınız.")
                oyuncu.ozellikGoster()
            else:
                baltali.saldir(oyuncu)
                print("Baltalı saldırısına uğradınız.")
                oyuncu.ozellikGoster()
        elif islem == "Baltalı Asker Saldırısı":
            baltali.saldir(oyuncu)
            print("Baltalı saldırısına uğradınız.")
            oyuncu.ozellikGoster()            
        elif islem == "Atlı Asker Saldırısı":
            atli.saldir(oyuncu)
            print("Atlı saldırısına uğradınız.")
            oyuncu.ozellikGoster()            
        elif islem == "Yeniçeri Asker Saldırısı":
            yeniceri.saldir(oyuncu)
            print("Yeniçeri saldırısına uğradınız.")
            oyuncu.ozellikGoster()            
        elif islem == "Mızraklı Asker Saldırısı":
            mizrakli.saldir(oyuncu)
            print("Mızraklı saldırısına uğradınız.")
            oyuncu.ozellikGoster()            
        elif islem == "Vahşi Doğa":
            oyuncu.can -= 5
            print("Vahşi doğada kaldınız.5 can düşüldü.")
            oyuncu.ozellikGoster() 
        elif islem == "Tuzak":
            sayi=random.randint(3,9)
            if sayi % 3 == 0:
                geriDonus=random.randint(2,5)
                new_harita.konum -= geriDonus
                self.aksionKarsiligi(new_harita.harita[new_harita.konum],oyuncu,new_harita)
                print("Haritada {} basamak geri gittiniz.".format(geriDonus))
            elif sayi % 4 == 0:
                yeniceri.saldir(oyuncu)
                atli.saldir(oyuncu)
                print("ikili saldırıya uğradınız.")
                oyuncu.ozellikGoster() 
            else :
                if len(oyuncu.ustundekiler) == 0:
                    print("Üstünüzde kıyafet yok")
                else:
                    randomUstundeki=random.randint(0,len(oyuncu.ustundekiler))
                    if oyuncu.ustundekiler[randomUstundeki] == hancer.adi:
                        hancer.kiyafetCikar(oyuncu)
                        print("Hançer çıkarıldı.")
                        oyuncu.ozellikGoster() 
                    elif oyuncu.ustundekiler[randomUstundeki] == kumas_elbise.adi:
                        
                        kumas_elbise.kiyafetCikar(oyuncu)
                        print("Kumaş elbise çıkarıldı.")
                        oyuncu.ozellikGoster() 

                    elif oyuncu.ustundekiler[randomUstundeki] == bileklik.adi:
                        
                        bileklik.kiyafetCikar(oyuncu)
                        print("Bileklik çıkarıldı.")
                        oyuncu.ozellikGoster() 
                       
                    elif oyuncu.ustundekiler[randomUstundeki] == kilic.adi:
                        
                        kilic.kiyafetCikar(oyuncu)
                        print("Kılıç çıkarıldı.")
                        oyuncu.ozellikGoster() 
                    
                    elif oyuncu.ustundekiler[randomUstundeki] == tahta_kalkan.adi:
                        
                        tahta_kalkan.kiyafetCikar(oyuncu)
                        print("Tahta kalkan çıkarıldı.")
                        oyuncu.ozellikGoster() 
                        
                    elif oyuncu.ustundekiler[randomUstundeki] == ayakkabi.adi:
                        
                        ayakkabi.kiyafetCikar(oyuncu)
                        print("Ayakkabı çıkarıldı.")
                        oyuncu.ozellikGoster()  
                    elif oyuncu.ustundekiler[randomUstundeki] == demir_kalkan.adi:
                        
                        demir_kalkan.kiyafetCikar(oyuncu)
                        print("Kalkan çıkarıldı.")
                        oyuncu.ozellikGoster() 
                        
                    elif oyuncu.ustundekiler[randomUstundeki] == mizrak.adi:
                        
                        mizrak.kiyafetCikar(oyuncu)
                        print("Mızrak çıkarıldı.")
                        oyuncu.ozellikGoster() 
                    
                    elif oyuncu.ustundekiler[randomUstundeki] == migfer.adi:
                        
                        migfer.kiyafetCikar(oyuncu)
                        print("Miğfer çıkarıldı.")
                        oyuncu.ozellikGoster() 
                                              
        elif islem == "Random İtem Kazan":
            derece=self.randomUret()
            derece1=random.randint(0,2)
            if derece == 1:
                if derece1 == 0:
                    oyuncu.kasa.append(hancer.adi)
                    hancer.mesaj()
                elif derece1 == 1:
                    oyuncu.kasa.append(kumas_elbise.adi)
                    kumas_elbise.mesaj()
                else:
                    oyuncu.kasa.append(bileklik.adi)
                    bileklik.mesaj()
            else: 
                if derece1 == 0:
                    oyuncu.kasa.append(kilic.adi)
                    kilic.mesaj()
                elif derece1 == 1:
                    oyuncu.kasa.append(tahta_kalkan.adi)
                    tahta_kalkan.mesaj()
                else:
                    oyuncu.kasa.append(ayakkabi.adi) 
                    ayakkabi.mesaj()
        elif islem == "Elit İtem Kazan":
            derece1=random.randint(0,2)
            if derece1 == 0:
                oyuncu.kasa.append(mizrak.adi)
                mizrak.mesaj()
            elif derece1 == 1:
                oyuncu.kasa.append(migfer.adi)
                migfer.mesaj()
            else:
                oyuncu.kasa.append(demir_kalkan.adi)
                demir_kalkan.mesaj()
        elif islem == "Han":
            oyuncu.can += 10
            print("Hana uğradınız ve 10 can kazandınız.")
            oyuncu.ozellikGoster() 
        elif islem == "Kıyafet Değiştirme Bölgesi":
            oyuncu.kasaListele()
            if len(oyuncu.kasa) == 0:
                print("Kasa boş kıyafet giyemiyorsunuz.")
            else:
                giyilecek=input("Giymek istediğiniz kıyafeti türkçe karakter kullanmadan giriniz.")
                if giyilecek.lower() == "hancer":
                    if self.kiyafetKontrol(oyuncu,hancer.adi):
                        if kilic.adi in oyuncu.ustundekiler:
                            kilic.kiyafetCikar(oyuncu)
                        if mizrak.adi in oyuncu.ustundekiler:
                            mizrak.kiyafetCikar(oyuncu)                    
                        hancer.kiyafetGiy(oyuncu)
                        print("Hançer giyildi.")
                        oyuncu.ozellikGoster() 
                    else:
                        print("Seni uyanık bu kiyafet zaten üstünde var ceza olarak hakkın yandı")
                elif giyilecek.lower() == "kumas elbise":
                    if self.kiyafetKontrol(oyuncu,kumas_elbise.adi):
                        kumas_elbise.kiyafetGiy(oyuncu)
                        print("Kumaş elbise giyildi.")
                        oyuncu.ozellikGoster() 
                    else:
                        print("Seni uyanık bu kiyafet zaten üstünde var ceza olarak hakkın yandı")
                elif giyilecek.lower() == "bileklik":
                    if self.kiyafetKontrol(oyuncu,bileklik.adi):
                        bileklik.kiyafetGiy(oyuncu)
                        print("Bileklik giyildi.")
                        oyuncu.ozellikGoster() 
                    else:
                        print("Seni uyanık bu kiyafet zaten üstünde var ceza olarak hakkın yandı")
                elif giyilecek.lower() == "kilic":
                    if self.kiyafetKontrol(oyuncu,kilic.adi):
                        if hancer.adi in oyuncu.ustundekiler:
                            hancer.kiyafetCikar(oyuncu)
                        if mizrak.adi in oyuncu.ustundekiler:
                            mizrak.kiyafetCikar(oyuncu)                     
                        kilic.kiyafetGiy(oyuncu)
                        print("Kılıç giyildi.")
                        oyuncu.ozellikGoster() 
                    else:
                        print("Seni uyanık bu kiyafet zaten üstünde var ceza olarak hakkın yandı")
                elif giyilecek.lower() == "tahta kalkan":
                    if self.kiyafetKontrol(oyuncu,tahta_kalkan.adi):
                        if demir_kalkan.adi in oyuncu.ustundekiler:
                            demir_kalkan.kiyafetCikar(oyuncu)                    
                        tahta_kalkan.kiyafetGiy(oyuncu)
                        print("Tahta kalkan giyildi.")
                        oyuncu.ozellikGoster() 
                    else:
                        print("Seni uyanık bu kiyafet zaten üstünde var ceza olarak hakkın yandı")
                elif giyilecek.lower() == "ayakkabi":
                    if self.kiyafetKontrol(oyuncu,ayakkabi.adi):
                        ayakkabi.kiyafetGiy(oyuncu)
                        print("Ayakkabı giyildi.")
                        oyuncu.ozellikGoster() 
                    else:
                        print("Seni uyanık bu kiyafet zaten üstünde var ceza olarak hakkın yandı")
                elif giyilecek.lower() == "kalkan":
                    if self.kiyafetKontrol(oyuncu,demir_kalkan.adi):
                        if tahta_kalkan in oyuncu.ustundekiler:
                            tahta_kalkan.kiyafetCikar(oyuncu)
                        demir_kalkan.kiyafetGiy(oyuncu)
                        print("Kalkan giyildi.")
                        oyuncu.ozellikGoster() 
                    else:
                        print("Seni uyanık bu kiyafet zaten üstünde var ceza olarak hakkın yandı")
                elif giyilecek.lower() == "mizrak":
                    if self.kiyafetKontrol(oyuncu,mizrak.adi):
                        if kilic.adi in oyuncu.ustundekiler:
                            kilic.kiyafetCikar(oyuncu)
                        if hancer.adi in oyuncu.ustundekiler:
                            hancer.kiyafetCikar(oyuncu)                     
                        mizrak.kiyafetGiy(oyuncu)
                        print("Mızrak giyildi.")
                        oyuncu.ozellikGoster() 
                    else:
                        print("Seni uyanık bu kiyafet zaten üstünde var ceza olarak hakkın yandı")
                elif giyilecek.lower() == "migfer":
                    if self.kiyafetKontrol(oyuncu,migfer.adi):
                        migfer.kiyafetGiy(oyuncu)
                        print("Miğfer giyildi.")
                        oyuncu.ozellikGoster() 
                    else:
                        print("Seni uyanık bu kiyafet zaten üstünde var ceza olarak hakkın yandı")   
                else:
                    print("Hatalı giriş oldu galiba tükçe karakter kullanmadan giriş yap lütfen")
                    self.aksionKarsiligi(islem,oyuncu,new_harita)
        elif islem == "SON":
            print("Tebrikler oyunun sonuna geldiniz.")
            sys.exit()
        else:
            print("Hatalı bir komut")
            

