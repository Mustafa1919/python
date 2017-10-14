def mors_translate(metin):
    alfabe="abcdefghijklmnopqrstuvwxyz1234567890"
    mors=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.",
          "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",".----","..---","...--","....-",".....",
          "-....","--...","---..","----.","-----"]
    kontrol="çığöşü"
    swap="cigosu"
    try :
        with open("Türkçe-Mors.txt","w") as file:
            for i in metin:
                if i in kontrol:
                    index_swap=kontrol.index(i)
                    i=swap[index_swap]
                if i == " ":
                    file.write("   ")
                elif i == "\n":
                    file.write("\n")
                else:
                    if i not in alfabe:
                        print("Hatalı harf girişi.Girilen harf: {}".format(i))
                        print("{} nolu harf yazılmadı".format(metin.index(i)+1))
                    else:
                        index=alfabe.index(i)
                        file.write("{} ".format(mors[index]))
    except IOError :
        print("Dosyalamada hata oluştu")
        
def türkçe_translate(metin):
    alfabe="abcdefghijklmnopqrstuvwxyz1234567890"
    mors=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.",
          "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",".----","..---","...--","....-",".....",
          "-....","--...","---..","----.","-----"]
    kontrol="çığöşü"
    swap="cigosu"
    try:
        with open("Mors-Türkçe.txt","w") as file:
            for i in metin.splitlines():
                for j in i.split("   "):
                    for k in j.split():
                        index=mors.index(k)
                        file.write(alfabe[index]),
                    file.write(" "),
                file.write("\n")
    except IOError:
        print("Dosya işlem hata")
                    
path=input("Dosya yolu: ")
try:
    with open(path,"r") as file:
        veri=file.read().lower()
        #print(veri)
        mors_translate(veri)
        türkçe_translate(veri)
except IOError:
    print("hata")
        
        



