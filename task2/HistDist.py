import math
import random

def triangle(a):
    for i in range(a+1):
        print(' '*(a-i)+'*'*i*2+'*')

def histDistance(hist1, hist2):
    quadsum = 0
    for i in range(len(hist1)):
        quadsum += (hist1[i]-hist2[i])**2
    return math.sqrt(quadsum)

def createRandHist(n = 3):
    rand_list=[0]*n
    for i in range(n):
        rand_list[i] = random.randint(0,100)
    return rand_list

def readHist(fName = "./RHist.txt"):
    file = open(fName, "r")
    a = file.read().split()
    return a

def writeHist(al, fName = "./WHist.txt"):
    file = open(fName, "w")
    file.write(' '.join(al))

triangle(4)

hist1 = createRandHist(2)
hist2 = createRandHist(2)
print("Декартово расстояние между",hist1, ",",hist2, "=", histDistance(hist1, hist2))

tt = readHist()
print("В файле:",tt)
writeHist(tt)