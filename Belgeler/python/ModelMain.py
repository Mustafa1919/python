import numpy as np
import ModelNormalize
import ModelRegresyon
import ModelSinirAğı

lengt=int(input("Kaç değer girilecek: "))
listeX=list(map(lambda x: float(input("x-->")),range(lengt)))
listeY=list(map(lambda y: float(input("y-->")),range(lengt)))

ModelRegresyon.Regresyon(np.array(listeX),np.array(listeY))
norListeX=ModelNormalize.Normalizasyon(np.array(listeX))
norListeY=ModelNormalize.Normalizasyon(np.array(listeY))
print(norListeX)
print(norListeY)

girisDeger=int(input("Sinir ağında kaç giriş uygulanacak: "))
araDeger=int(input("Sinir ağında kaç ara katman oluşturulacak: "))
agirlik=ModelSinirAğı.SinirAgiAgirlik(girisDeger,araDeger)
print(agirlik)
print(ModelSinirAğı.SinirAgiCiktisi(agirlik,norListeX,girisDeger,araDeger))