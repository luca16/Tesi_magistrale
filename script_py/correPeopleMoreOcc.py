from scipy.stats.stats import pearsonr
import json
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import caricamento
from caricamento import *
from people import *


# ritorna il numero di occorrenze di un nome
def getOcc(date, name):
    con = 1
    for p in people:
        if p[1] == name and date != p[0] :
            con=con+1
    return con

peopleOcc = []

for p in people:
    occ = getOcc(p[0],p[1])
    peopleOcc.append([p,occ])

#array contenente le persone che hanno più occorrenze
newPeople=[]

for o in peopleOcc:
    if o[1] > 1 :
        newPeople.append(o[0])


# ritona 1 se il nome è presente in una data, 0 altrimenti     
def checkPerson(d,name):
    for p in newPeople:
        if (p[0]==d):
            if (p[1]==name):
                return 1
    return 0

nameList = []

for p in newPeople:
    nameList.append(p[1])


def removeDuplicate(x):
  return list(dict.fromkeys(x))

nameList = removeDuplicate(nameList)

#contiene la coppia -> (namePerson,segnale) dove segnale è un array con 1 se il nome è presente in quella data, 0 altrimenti 
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

#rimuove le coppie di un nome con se stesso
for c in coppie:
    if c[0]==c[1]:
        coppie.remove(c)


def Sort(sub_li): 
    sub_li.sort(key = lambda x: x[2],reverse=True) 
    return sub_li

#ordino le coppie in base al valore del coefficiente di correlazioni
coppie = Sort(coppie) 


#coppie.pop(len(coppie)-1)
nameList.pop(len(nameList)-1)

def personMoreCorrelation(name):    
    for c in coppie:
        if c[0]==name:
            return c

#contiene le coppie più correlate
moreCor =[]

prov = nameList

for n in prov:   
    coup = personMoreCorrelation(n)
    if not exist(moreCor,coup):
        moreCor.append(coup)
        

newMorCorr = moreCor

def removeCouple(n):
    for l in newMorCorr:
        if l[0] == n :
            newMorCorr.remove(l)
           
        
    

print(moreCor)

#scandico l'array se per ogni nome aggiungo la coppia 
# più correlata, rimuova dall'array la coppia con cui era correlato
#  il secondo nome in quanto gia l'ho accoppiato

ex = []


for m in newMorCorr:
    ex.append(m)
    print(m)
    removeCouple(m[1])
 


print("")
print(ex) 

topten = []

for u in range(0,11):
    topten.append(ex[u])


print("")
print(topten) 

#aggiungo le date
finish = []

for mo in topten:
    for p in people:
        if(mo[0]==p[1]):
            finish.append([p[0],p[1]])
        if(mo[1]==p[1]):
            finish.append([p[0],p[1]])
   



"""
#create json file

with open('/home/luca/Scrivania/javascript/correlationPeople.json', 'w') as f:
    f.write("{ \n \"correlationpeople\" :  [\n")
    for item in finish:
        f.write("       { \"date\": \"%s\"," %item[0])
        f.write(" \"name\": \"%s\"" %item[1])
        f.write("},\n")
    f.write("       ]\n")
    f.write("}\n")

"""
with open('/home/luca/Scrivania/javascript/topTenCorrelationPeople.json', 'w') as f:
    f.write("{ \n \"correlationpeople\" :  [\n")
    for item in finish:
        f.write("       { \"date\": \"%s\"," %item[0])
        f.write(" \"name\": \"%s\"" %item[1])
        f.write("},\n")
    f.write("       ]\n")
    f.write("}\n")