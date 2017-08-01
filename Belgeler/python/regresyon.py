def Regresyon():
    leng=int(input("Modele kaç değer girilecek: "))
    print("Sırayla x değerlerini giriniz.")
    xReg=list(map(lambda x: int(input("x--> ")),range(leng)))
    yReg=list(map(lambda y: int(input("y--> ")),range(leng)))
    #print(yReg , xReg)
    yToplam,xXy,xKare,xToplam=0,0,0,0
    #print(yToplam , xXy , xKare , xToplam)
    for i in range(leng):
        xToplam+=xReg[i]
        yToplam+=yReg[i]
        xXy+=(xReg[i]*yReg[i])
        xKare+=(xReg[i]**2)
    #print(yToplam , xXy , xKare , xToplam)
    kat=xKare/xToplam
    if kat>=0:
        kb=leng*(-1*kat)
        ke=yToplam*(-1*kat)
    elif kat<0:
        kb=kat*leng
        ke=yToplam*kat
    y=(ke+xXy)/(kb+xToplam)
    x=(yToplam-leng*y)/xToplam
    print("Regresyon Denklem= %.2f x + %.2f " %(x,y)) 
Regresyon()