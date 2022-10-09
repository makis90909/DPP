from configparser import MAX_INTERPOLATION_DEPTH
import time
import random
from xmlrpc.client import MAXINT

def initListWithRandomNumbers():
    n = 1000
    rand_list=[0]*n
    for i in range(n):
        rand_list[i] = random.randint(0,999)
    return rand_list
    
def calcHist(tdata):
    hist = [0]*10
    for i in tdata:
        hist[i//100] += 1
    return hist

def TimeScore():
    a = initListWithRandomNumbers()
    start = time.time()
    calcHist(a)
    end = time.time()
    return end - start
    
t = 100
minT = MAXINT
maxT = 0
sumT = 0
for i in range(t):
    res = TimeScore()
    sumT += res
    if res < minT: minT = res 
    if res > maxT: maxT = res
print("Минимальное время работы ", minT)
print("Максимальное время работы ", maxT)
print("Среднее время работы ", sumT / t)
