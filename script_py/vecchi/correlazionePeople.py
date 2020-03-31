from scipy.stats.stats import pearsonr
import json
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import caricamento
from caricamento import *
from people import *


def checkPerson(d,name):
    for p in people:
        if (p[0]==d):
            if (p[1]==name):
                return 1
    return 0

nameList = []

for p in people:
    nameList.append(p[1])


def removeDuplicate(x):
  return list(dict.fromkeys(x))

nameList = removeDuplicate(nameList)

out = []


for n in nameList:
    sign = []
    for d in date:
        check = checkPerson(d,n)
        sign.append(check)
        
    out.append([n,sign])

def exist(arr,item):
    for c in arr:
        if c[0] == item[0] and c[1] == item[1] or c[0]==item[1] and c[1]== item[0] :
                return True
    return False   

coppie = []

for name1 in out:
    for name2 in out:
        x = name1[1]
        y = name2[1]
        coef,_ = pearsonr(x,y)
        item = [name1[0],name2[0],coef]
        if(not(exist(coppie,item))):
            coppie.append(item)

for c in coppie:
    if c[0]==c[1]:
        coppie.remove(c)


def Sort(sub_li): 
    sub_li.sort(key = lambda x: x[2],reverse=True) 
    return sub_li
  
coppie = Sort(coppie) 
#print(coppie) 

coppie.pop(len(coppie)-1)
nameList.pop(len(nameList)-1)

def correlation (name):
    
    for c in coppie:
        if c[0]==name:
            return c

moreCor =[]

prova = nameList
for n in prova:   
    coup = correlation(n)
    if not exist(moreCor,coup):
        moreCor.append(coup)
        
print(moreCor)

def removeCouple(lista, n):
    for l in lista:
        if l[0] == n:
            lista.remove(l)
    return lista


ex = []
pippo = moreCor
for m in pippo:
    ex.append(m)
    removeCouple(pippo,m[1])


print(ex)



finish = []

for mo in ex:
    for p in people:
        if(mo[0]==p[1]):
            finish.append([p[0],p[1]])
        if(mo[1]==p[1]):
            finish.append([p[0],p[1]])
    

print(finish)