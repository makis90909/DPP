import random
import math

class NNClassifier:
    type = None
    def __init__(self, a):
        self.hist = a
    
    def readObj(self, fname = "./listObj.txt"):
        file = open(fname)

        a = file.readlines()
        a = [x.split() for x in a]
        
        self.listObj = []
        for i in a:
            self.listObj.append([i[0], histDistance(self.hist, [int(x) for x in i[1:]])])
        min = 0
        for i in range(len(self.listObj)):
            min = i
            for j in range(i, len(self.listObj)):
                if self.listObj[j][1] < self.listObj[min][1]:
                    min = j
            self.listObj[min], self.listObj[i] = self.listObj[i], self.listObj[min]
        
    def typeClass(self):
        len = 3
        a = self.listObj[:len]

        types = dict.fromkeys([x[0] for x in a], 0)
        for i in a:
            types[i[0]]+=1
        max = a[0][0]
        for i in types.keys():
            if types[i] > types[max]:
                max = i
        self.type = max

def histDistance(hist1, hist2):
    quadsum = 0
    for i in range(len(hist1)):
        quadsum += (hist1[i]-hist2[i])**2
    return math.sqrt(quadsum)

def RandList(n = 3):
    a = [0]*n
    for i in range(n):
        a[i] = random.randint(0, 100)
    return a

cl1 = NNClassifier(RandList())
cl1.readObj()
cl1.typeClass()
print(cl1.type)