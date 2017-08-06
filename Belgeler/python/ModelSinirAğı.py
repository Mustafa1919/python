import numpy as np
def SinirAgiAgirlik(girisSayisi , araKatman):
    a=[]
    for i in range(girisSayisi+1):
        for j in range(araKatman):
            a.append(np.random.uniform(-1,1))
    agirlik=np.array(a)
    agirlik.resize(girisSayisi+1,araKatman)
    return agirlik

def SinirAgiCiktisi(listAgirlik,listX,giris,ara):
    print(listX)
    girisDegeri=[]
    araToplam=[]
    toplam,toplamCikis=0,0
    for i in range(giris):
        girisDegeri.append(int(input("X verilerinden kaç nolu girdiler kullanılacak: ")))
        print(listX[girisDegeri[i]])
    for i in range(ara):
        for j in range(giris):
            toplam+=listX[girisDegeri[j]]*listAgirlik[j,i]
        araToplam.append(1/(1+np.exp(-1*toplam)))
    print(araToplam)
    for i in range(ara):
        toplamCikis+=(araToplam[i]*listAgirlik[giris,i])
    return 1/(1+np.exp(-1*toplamCikis))
        
        
            
            
            