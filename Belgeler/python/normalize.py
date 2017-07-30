def normalize():
    uzunluk=int(input("Kaç değer girilecek: "))
    liste=list(map(lambda x: float(input("Değeri giriniz: ")),range(uzunluk)))
    def minBul():
        mind=999999
        for i in liste:
            if mind>i:
                mind=i
        return mind
    def maxBul():
        maxd=0
        for i in liste:
            if maxd<i:
                maxd=i
        return maxd
    mink=minBul()
    maxk=maxBul()
    def f(x):
        return 0.1+((x-mink)/(maxk-mink))*0.8
    print(list(map(f,liste)))
normalize()
