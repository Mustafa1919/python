from time import sleep
tahta=[["___","___","___"],["___","___","___"],["___","___","___"]]
kazanma_olcutleri = [[[0, 0], [1, 0], [2, 0]],
                    [[0, 1], [1, 1], [2, 1]],
                    [[0, 2], [1, 2], [2, 2]],
                    [[0, 0], [0, 1], [0, 2]],
                    [[1, 0], [1, 1], [1, 2]],
                    [[2, 0], [2, 1], [2, 2]],
                    [[0, 0], [1, 1], [2, 2]],
                    [[0, 2], [1, 1], [2, 0]]]
o_durum=[]
x_durum=[]
print("\n"*15)
for i in tahta:
    print("\t".expandtabs(30), *i, end="\n"*2)
sira=1
while True:
    if sira % 2 == 0:
        isaret= "X".center(3)
    else:
        isaret= "O".center(3)
    print()
    print("ISARET: {} \n".format(isaret))
    x = input("yukaridan asagiya [1,2,3]: ".ljust(30))
    if x=="q":
        break
    y=input("soldan saga [1,2,3]: ".ljust(30))
    if y=="q":
        break
    x=int(x)-1
    y=int(y)-1
    print("\n"*15)
    if tahta[x][y] == "___":
        tahta[x][y]=isaret
        if isaret == "X".center(3):
            x_durum +=[[x,y]]
        elif isaret == "O".center(3):
            o_durum +=[[x,y]]
        sira +=1
    else:
        print("\nOrasi dolu")
    for i in tahta:
        print("\t".expandtabs(30), *i , end="\n"*2)
    for i in kazanma_olcutleri:
        o=[z for z in i if z in o_durum]
        x=[z for z in i if z in x_durum]
        if len(o) == len(i):
            print("O kazandi")
            quit()
        if len(x) == len(i):
            print("X kazandi")
            quit()