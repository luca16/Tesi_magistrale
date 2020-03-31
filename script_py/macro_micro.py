import json
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import caricamento
from caricamento import *

#############################  CATEGORIE ########################

categorie = []

# per il giorn 08-10 
for i in range (0, len(f0810a['RESPONSE']['CATEGORIZATION'])):
    cat = f0810a['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f0810a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f0810a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f0810a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["08-10-19",cat,name,freq])

for i in range (0, len(f0810b['RESPONSE']['CATEGORIZATION'])):
    cat = f0810b['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f0810b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f0810b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f0810b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["08-10-19",cat,name,freq])

# per il giorn 11-10 
for i in range (0, len(f1110a['RESPONSE']['CATEGORIZATION'])):
    cat = f1110a['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f1110a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f1110a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f1110a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["11-10-19",cat,name,freq])


# per il giorn 14-10 
for i in range (0, len(f1410a['RESPONSE']['CATEGORIZATION'])):
    cat = f1410a['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f1410a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f1410a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f1410a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["14-10-19",cat,name,freq])

for i in range (0, len(f1410b['RESPONSE']['CATEGORIZATION'])):
    cat = f1410b['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f1410b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f1410b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f1410b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["14-10-19",cat,name,freq])

# per il giorn 08-11 
for i in range (0, len(f0811a['RESPONSE']['CATEGORIZATION'])):
    cat = f0811a['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f0811a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f0811a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f0811a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["08-11-19",cat,name,freq])

for i in range (0, len(f0811b['RESPONSE']['CATEGORIZATION'])):
    cat = f0811b['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f0811b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f0811b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f0811b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["08-11-19",cat,name,freq])

# per il giorn 09-11 
for i in range (0, len(f0911a['RESPONSE']['CATEGORIZATION'])):
    cat = f0911a['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f0911a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f0911a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f0911a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["09-11-19",cat,name,freq])

# per il giorn 11-11 
for i in range (0, len(f1111a['RESPONSE']['CATEGORIZATION'])):
    cat = f1111a['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f1111a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f1111a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f1111a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["11-11-19",cat,name,freq])

for i in range (0, len(f1111b['RESPONSE']['CATEGORIZATION'])):
    cat = f1111b['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f1111b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f1111b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f1111b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["11-11-19",cat,name,freq])

# per il giorn 20-11 
for i in range (0, len(f2011a['RESPONSE']['CATEGORIZATION'])):
    cat = f2011a['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f2011a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f2011a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f2011a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["20-11-19",cat,name,freq])

# per il giorn 21-11 
for i in range (0, len(f2111a['RESPONSE']['CATEGORIZATION'])):
    cat = f2111a['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f2111a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f2111a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f2111a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["21-11-19",cat,name,freq])

for i in range (0, len(f2111b['RESPONSE']['CATEGORIZATION'])):
    cat = f2111b['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f2111b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f2111b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f2111b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["21-11-19",cat,name,freq])

for i in range (0, len(f2111c['RESPONSE']['CATEGORIZATION'])):
    cat = f2111c['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f2111c['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f2111c['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f2111c['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["21-11-19",cat,name,freq])

# per il giorn 22-11 
for i in range (0, len(f2211a['RESPONSE']['CATEGORIZATION'])):
    cat = f2211a['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f2211a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f2211a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f2211a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["22-11-19",cat,name,freq])

for i in range (0, len(f2211b['RESPONSE']['CATEGORIZATION'])):
    cat = f2211b['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f2211b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f2211b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f2211b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["22-11-19",cat,name,freq])

# per il giorn 25-11 
for i in range (0, len(f2511a['RESPONSE']['CATEGORIZATION'])):
    cat = f2511a['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f2511a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f2511a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f2511a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["25-11-19",cat,name,freq])

for i in range (0, len(f2511b['RESPONSE']['CATEGORIZATION'])):
    cat = f2511b['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f2511b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f2511b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f2511b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["25-11-19",cat,name,freq])



# per il giorn 04-12
for i in range (0, len(f0412a['RESPONSE']['CATEGORIZATION'])):
    cat = f0412a['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f0412a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f0412a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f0412a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["04-12-19",cat,name,freq])

for i in range (0, len(f0412b['RESPONSE']['CATEGORIZATION'])):
    cat = f0412b['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f0412b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f0412b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f0412b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["04-12-19",cat,name,freq])

# per il giorn 09-12 
for i in range (0, len(f0912a['RESPONSE']['CATEGORIZATION'])):
    cat = f0912a['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f0912a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f0912a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f0912a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["09-12-19",cat,name,freq])

for i in range (0, len(f0912b['RESPONSE']['CATEGORIZATION'])):
    cat = f0912b['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f0912b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f0912b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f0912b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["09-12-19",cat,name,freq])

# per il giorn 10-12 
for i in range (0, len(f1012a['RESPONSE']['CATEGORIZATION'])):
    cat = f1012a['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f1012a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f1012a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f1012a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["10-12-19",cat,name,freq])


# per il giorn 13-12 
for i in range (0, len(f1312a['RESPONSE']['CATEGORIZATION'])):
    cat = f1312a['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f1312a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f1312a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f1312a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["13-12-19",cat,name,freq])

# per il giorn 14-12
for i in range (0, len(f1412a['RESPONSE']['CATEGORIZATION'])):
    cat = f1412a['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f1412a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f1412a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f1412a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["14-12-19",cat,name,freq])

# per il giorn 15-12 
for i in range (0, len(f1512a['RESPONSE']['CATEGORIZATION'])):
    cat = f1512a['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f1512a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f1512a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f1512a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["15-12-19",cat,name,freq])

for i in range (0, len(f1512b['RESPONSE']['CATEGORIZATION'])):
    cat = f1512b['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f1512b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f1512b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f1512b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["15-12-19",cat,name,freq])

# per il giorn 18-12 
for i in range (0, len(f1812a['RESPONSE']['CATEGORIZATION'])):
    cat = f1812a['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f1812a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f1812a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f1812a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["18-12-19",cat,name,freq])

for i in range (0, len(f1812b['RESPONSE']['CATEGORIZATION'])):
    cat = f1812b['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f1812b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f1812b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f1812b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["18-12-19",cat,name,freq])

# per il giorn 19-12 
for i in range (0, len(f1912a['RESPONSE']['CATEGORIZATION'])):
    cat = f1912a['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f1912a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f1912a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f1912a['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["19-12-19",cat,name,freq])

for i in range (0, len(f1912b['RESPONSE']['CATEGORIZATION'])):
    cat = f1912b['RESPONSE']['CATEGORIZATION'][i]["FEATURE"]
    for j in range(0,len(f1912b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'])):
        name = f1912b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['NAME']
        freq = f1912b['RESPONSE']['CATEGORIZATION'][i]['DOMAIN'][j]['FREQUENCY']
        categorie.append(["19-12-19",cat,name,freq])

#with open('/home/luca/Scrivania/javascript/categorie.txt', 'w') as f:
 #   for item in categorie:
  #      f.write("%s," % item)


#with open('/home/luca/Scrivania/javascript/categorie.json', 'w') as f:
 #   f.write("{ \n \"categorie\" :  [\n")
  #  for item in categorie:
   #     f.write("       { \"date\": \"%s\"," %item[0])
    #    f.write(" \"macroname\": \"%s\"," %item[1])
     #   f.write(" \"microname\": \"%s\"," %item[2])
      #  f.write(" \"frequency\": \"%s\"" %item[3])
       # f.write("},\n")
    #f.write("       ]\n")
    #f.write("}\n")

def getRows (date,cat):
    a = []
    for c in categorie:
        if c[0] == date :
            if c[1] == cat:
                a.append(c)
    return a 

# ordina per ogni data le categorie secondo l'ordine di macro 
macro = ["INTELLIGENCE","CYBERCRIME","CRIME","TERRORISM","GEOGRAPHY","EMOTIONS"]

out =[]

for d in date:
    for m in macro:
        out.append(getRows(d,m))

 
flat = []
for o in out :
    for s in o:
        flat.append(s)
"""
with open('/home/luca/Scrivania/javascript/categorie.json', 'w') as f:
    f.write("{ \n \"categorie\" :  [\n")
    for item in flat:
        f.write("       { \"date\": \"%s\"," %item[0])
        f.write(" \"macroname\": \"%s\"," %item[1])
        f.write(" \"microname\": \"%s\"," %item[2])
        f.write(" \"frequency\": \"%s\"" %item[3])
        f.write("},\n")
    f.write("       ]\n")
    f.write("}\n")

"""

# invece di ordinare per ogni data prendo tutti i dati rilativi alle categorie e li ordino per categoria
perCategoria=[]

for m in macro:
    for c in categorie:
        if (c[1]==m):
            perCategoria.append(c)

print("per categoria")

with open('/home/luca/Scrivania/javascript/percategorie.json', 'w') as f:
    f.write("{ \n \"categorie\" :  [\n")
    for item in perCategoria:
        f.write("       { \"date\": \"%s\"," %item[0])
        f.write(" \"macroname\": \"%s\"," %item[1])
        f.write(" \"microname\": \"%s\"," %item[2])
        f.write(" \"frequency\": \"%s\"" %item[3])
        f.write("},\n")
    f.write("       ]\n")
    f.write("}\n")


