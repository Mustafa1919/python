#-*-encoding=utf-8-*-
import numpy as np
class Breadth():
    def __init__(self):
        self.kontrolParent=6
        self.path=[]
    def breadth(self,tree):
        for i in tree:
            for j in i:
                if j[1] == 6:
                    self.path.append(j[0])
                    newKonum=j[2]
                    for k in range(5,-1,-1):
                        swap=tree[k][newKonum-1]
                        self.path.append(swap[0])
                        newKonum=swap[2]
                    self.path.reverse()
                    print(self.path)
                    break
class Depth():
    def __init__(self):
        self.kontrolParent=6
        self.path=[]
        self.flush=[]
    def depth(self,tree):
        self.flush.extend(tree[0])
        while True:
            ara=self.flush.pop(0)
            if ara[1] == 6:
                self.path.append(ara[0])
                newKonum=ara[2]
                for k in range(5,-1,-1):
                    swap=tree[k][newKonum-1]
                    self.path.append(swap[0])
                    newKonum=swap[2]
                self.path.reverse()
                print(self.path)
                break 
            araci=tree[ara[1]+1] 
            sayac=0
            for j in tree[ara[1]]: # bu ikisinin eşitliğini karşılaştırma
                if self.karsilastir(j[0],ara[0]):
                    konum=sayac
                    break
                sayac += 1
                
            for i in araci:
                if i[2]==konum+1:
                    self.flush.insert(1,i)
    def karsilastir(self,x,y):
        for i in range(len(x)):
            for j in range(len(x[i])):
                if x[i][j] != y[i][j]:
                    return False
        return True
            
            
            
                        
                


