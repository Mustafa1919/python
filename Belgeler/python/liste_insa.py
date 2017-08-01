l=[]
#** üssünü alır
for x in range(10):
    l.append(x**2)
print(l)
print(x)
#lambda isimsiz fonksiyon bu fonksiyon x'in karesini alıyor x diye bi değişken alıyor 
#kullanımdaki amaç for da x dışarda da tanımlı oluyor ama burada x döngü dışında tanımlı değil
squares=list(map(lambda x: x**2,range(10)))
print(squares)

def f(x):
    return x+5
l2=[2,8,3]
#burada f fonksiyonunu l2 listesine uygulayıp listeye çevirdik 
print(list(map(f,l2)))

#bir diğer kullanımda şudur ama burda da z döngü dışında tanımlı ve istemediğimiz bir durumdur
l3=[z**2 for z in range(10)]
print(l3)


#iç içe for yazımıda şöyledir
l4=[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(l4)
#3'lü kombinasyonuda şöyledir
l5=[(x,y,z) for x in [1,2,3] for y,z in [(1,2),(2,3),(3,4)] if x!=y]
print(l5)

