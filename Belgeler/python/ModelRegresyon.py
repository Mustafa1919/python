import numpy as np
def Regresyon(verisetX,verisetY):
    toplamY=np.sum(verisetY)
    toplamX=np.sum(verisetX)
    kareX=np.sum(np.square(verisetX))
    xXy=np.sum(verisetX*verisetY)
    kat=toplamX/(len(verisetX))
    if kat>=0:
        kat*=-1
    a=((toplamY*kat)-xXy)/((toplamX*kat)-kareX)
    b=(toplamY-(toplamX*a))/len(verisetX)
    print("Model = {0:.5f}x + {1:.5f}".format(a,b))
        
"""x=np.array(np.random.random(10)*100)
y=np.array(np.random.random(10)*100)
print(x )
print(y )
Regresyon(x,y)"""