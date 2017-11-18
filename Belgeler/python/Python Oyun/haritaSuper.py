#-*-encoding=utf-8-*-
import random
class HaritaSuper():
    def __init__(self):
        self.harita=("Basla","Buraya Zar Gelmez","Bonus","Random Askeri Saldırı","Random İtem Kazan","Vahşi Doğa","Baltalı Asker Saldırısı",
                "Tuzak","Random İtem Kazan","Elit İtem Kazan","Atlı Asker Saldırısı","Mızraklı Asker Saldırısı","Random İtem Kazan",
                "Kıyafet Değiştirme Bölgesi","Bonus","Yeniçeri Asker Saldırısı","Vahşi Doğa","Random İtem Kazan","Atlı Asker Saldırısı",
                "Random Askeri Saldırı","Baltalı Asker Saldırısı","Tuzak","Han","Kıyafet Değiştirme Bölgesi","Elit İtem Kazan",
                "Random İtem Kazan","Mızraklı Asker Saldırısı","Yeniçeri Asker Saldırısı","Random İtem Kazan","Vahşi Doğa",
                "Random Askeri Saldırı","Atlı Asker Saldırısı","Elit İtem Kazan","Baltalı Asker Saldırısı","Han","Kıyafet Değiştirme Bölgesi",
                "Random İtem Kazan","Yeniçeri Asker Saldırısı","Mızraklı Asker Saldırısı","Tuzak","Baltalı Asker Saldırısı",
                "Random Askeri Saldırı","Vahşi Doğa","Kıyafet Değiştirme Bölgesi","Random İtem Kazan","Han","Random Askeri Saldırı",
                "Tuzak","Random İtem Kazan","Kıyafet Değiştirme Bölgesi","Mızraklı Asker Saldırısı","Han","Random İtem Kazan",
                "Kıyafet Değiştirme Bölgesi","Tuzak","Yeniçeri Asker Saldırısı","Atlı Asker Saldırısı","Mızraklı Asker Saldırısı","SON")
        self.konum=0
        self.haritaOzellik={"Random Askeri Saldırı":"Rastgele Bir Tür Asker Sana Saldırır","Baltalı Asker Saldırısı":"Baltalı Asker Saldırır",
                       "Atlı Asker Saldırısı":"Atlı Asker Saldırır","Yeniçeri Asker Saldırısı":"Yeniçerinin Saldırısına Uğrarsın",
                       "Mızraklı Asker Saldırısı":"Mızraklı Asker Saldırır","Vahşi Doğa":"5 Canını Emer","Tuzak":"(2-5)Adım Geri Dön & "+
                       "Rastgele Kıyafetini Kaybet & Rastgele 2 Asker Saldırısına Uğrarsın","Random İtem Kazan":"1. veya 2. Seviye "+
                       "İtem Kazanırsın","Elit İtem Kazan":"Elit Seviye İtem Kazanırsın","Bonus":"Güçlü Bir At Kazanırsın",
                       "Han":"10 Can Ekler","Kıyafet Değiştirme Bölgesi":"Kasandaki Kıyafetleri Giymeni Sağlar"}
        
    def haritaGoster(self):
        for i in self.harita:
            print("{:^25}".format(i))
        
    def haritaOzellikleri(self):
        for key,value in self.haritaOzellik.items():
            print("{:<25}-->{}".format(key,value))
            
    
        
        
        
        
