print("Dosya yolu Linux için = /home/kullanıcıAdı/Belgeler/deneme.txt")
print("{:>21} = C:\\kullanıcıAdı\\belgeler\\deneme.txt" .format("Windows için"))
path=input("Analizi yapılcak dosya yolunu giriniz: ")
alfabe="abcçdefgğhıijklmnoöprsştuüvyz"

try:
    dosya=open(path,"r")
    veri1=dosya.read().lower()
    print(veri1)
    for i in alfabe:
        adet=veri1.count(i)
        if adet > 0:
            print("{:>3} adet {} vardır." .format(adet,i))
    dosya.close()
except IOError as e:
    print("Dosya işlemlerinde bir hata oluştu: {}" .format(e))
except :
    print("Beklenmeyen bi hata oluştu: {}")
    