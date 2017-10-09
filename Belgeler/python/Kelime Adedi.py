print("Kelime adet analizi için yolu giriniz.")
print("{:>26} şu şekilde = /home/kullanıcıAdı/deneme.txt" .format("Linux için"))
print("{:>26} şu şekilde = C:\\kullanıcıAdı\\deneme.txt".format("Wndows için"))
path=input("Yol : ")
liste=[]
frekans=[]
try :
    file=open(path,"r")
    veri=file.read().lower().split()
    for i in veri:
        if i not in liste:
            liste.append(i)
    for i in liste:
        print("{:>15} kelimesi {:^5} adet geçmektedir.".format(i,veri.count(i)))
    file.close()
except IOError as e:
    print("Dosya işlemde sorun oldu"+e)