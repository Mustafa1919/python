print("Kelime analizi için yolu giriniz.")
print("{:>26} şu şekilde = /home/kullanıcıAdı/deneme.txt" .format("Linux için"))
print("{:>26} şu şekilde = C:\\kullanıcıAdı\\deneme.txt" .format("Windows için"))
path=input("Yol : ")
liste=[0,0,0,0,0,0,0,0,0,0,0,0]
try:
    file=open(path,"r")
    veri=file.read().lower().split()
    for i in veri:
        liste[len(i)-1] += 1
    file.close()
except IOError as e:
    print("Dosya işleminde bir hata oluştu"+e)
for i in range(12):
    print("{:>4} uzunluğunda kelime {:>4} adet var" .format((i+1),liste[i]))