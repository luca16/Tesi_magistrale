import json
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import caricamento
from caricamento import *


# persone
people = []



#array coppie data nome per il gorno 08-10

for i in range(0,(len(f0810a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f0810a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["08-10-19",a])
for i in range(0,(len(f0810b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f0810b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["08-10-19",b])



#array coppie data nome per il gorno 11-10
for i in range(0,(len(f1110a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f1110a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["11-10-19",a])

#array coppie data nome per il gorno 14-10
for i in range(0,(len(f1410a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f1410a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["14-10-19",a])
for i in range(0,(len(f1410b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f1410b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["14-10-19",b])


#array coppie data nome per il gorno 22-10
for i in range(0,(len(f2210a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f2210a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["22-10-19",a])
for i in range(0,(len(f2210b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f2210b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["22-10-19",b])

#array coppie data nome per il gorno 31-10

for i in range(0,(len(f3110a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f3110a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["31-10-19",a])
for i in range(0,(len(f3110b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f3110b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["31-10-19",b])


#array coppie data nome per il gorno 08-11
for i in range(0,(len(f0811a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f0811a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["08-11-19",a])
for i in range(0,(len(f0811b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f0811b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["08-11-19",b])

#array coppie data nome per il gorno 09-11
for i in range(0,(len(f0911a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f0911a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["09-11-19",a])

#array coppie data nome per il gorno 11-11
for i in range(0,(len(f1111a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f1111a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["11-11-19",a])
for i in range(0,(len(f1111b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f1111b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["11-11-19",b])

#array coppie data nome per il gorno 14-11
for i in range(0,(len(f1411a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f1411a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["14-11-19",a])

#array coppie data nome per il gorno 15-11
for i in range(0,(len(f1511a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f1511a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["15-11-19",a])
for i in range(0,(len(f1511b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f1511b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["15-11-19",b])

#array coppie data nome per il gorno 19-11
for i in range(0,(len(f1911a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f1911a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["19-11-19",a])

#array coppie data nome per il gorno 20-11
for i in range(0,(len(f2011a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f2011a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["20-11-19",a])

#array coppie data nome per il gorno 21-11
for i in range(0,(len(f2111a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f2111a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["21-11-19",a])
for i in range(0,(len(f2111b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f2111b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["21-11-19",b])
for i in range(0,(len(f2111c['RESPONSE']['PEOPLE']['PERSON']))):
    c = f2111c['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["21-11-19",c])

#array coppie data nome per il gorno 22-11
for i in range(0,(len(f2211a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f2211a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["22-11-19",a])
for i in range(0,(len(f2211b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f2211b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["22-11-19",b])

#array coppie data nome per il gorno 25-11
for i in range(0,(len(f2511a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f2511a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["25-11-19",a])
for i in range(0,(len(f2511b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f2511b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["25-11-19",b])

#array coppie data nome per il gorno 26-11

for i in range(0,(len(f2111b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f2611b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["26-11-19",b])


#array coppie data nome per il gorno 04-12
for i in range(0,(len(f0412a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f0412a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["04-12-19",a])
for i in range(0,(len(f0412b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f0412b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["04-12-19",b])

#array coppie data nome per il gorno 09-12
for i in range(0,(len(f0912a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f0912a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["09-12-19",a])
for i in range(0,(len(f0912b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f0912b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["09-12-19",b])

#array coppie data nome per il gorno 10-12
for i in range(0,(len(f1012a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f1012a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["10-12-19",a])

#array coppie data nome per il gorno 13-12
for i in range(0,(len(f1312a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f1312a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["13-12-19",a])

for i in range(0,(len(f1412a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f1412a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["14-12-19",a])

#array coppie data nome per il gorno 15-12
for i in range(0,(len(f1512a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f1512a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["15-12-19",a])
for i in range(0,(len(f1512b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f1512b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["15-12-19",b])

#array coppie data nome per il gorno 18-12
for i in range(0,(len(f1812a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f1812a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["18-12-19",a])
for i in range(0,(len(f1812b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f1812b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["18-12-19",b])


#array coppie data nome per il gorno 19-12
for i in range(0,(len(f1912a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f1912a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["19-12-19",a])
for i in range(0,(len(f1912b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f1912b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["19-12-19",b])

#array coppie data nome per il gorno 21-01
for i in range(0,(len(f2101a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f2101a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["21-01-20",a])

#array coppie data nome per il gorno 22-01
for i in range(0,(len(f2201a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f2201a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["22-01-20",a])
for i in range(0,(len(f2201b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f2201b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["22-01-20",b])
for i in range(0,(len(f2201c['RESPONSE']['PEOPLE']['PERSON']))):
    c = f2201c['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["22-01-20",c])
for i in range(0,(len(f2201d['RESPONSE']['PEOPLE']['PERSON']))):
    d = f2201d['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["22-01-20",d])
for i in range(0,(len(f2201e['RESPONSE']['PEOPLE']['PERSON']))):
    e = f2201e['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["22-01-20",e])

#array coppie data nome per il gorno 23-01
for i in range(0,(len(f2301a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f2301a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["23-01-20",a])
for i in range(0,(len(f2301b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f2301b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["23-01-20",b])
for i in range(0,(len(f2301c['RESPONSE']['PEOPLE']['PERSON']))):
    c = f2301c['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["23-01-20",c])
for i in range(0,(len(f2301d['RESPONSE']['PEOPLE']['PERSON']))):
    d = f2301d['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["23-01-20",d])

#array coppie data nome per il gorno 24-01
for i in range(0,(len(f2401a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f2401a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["24-01-20",a])
for i in range(0,(len(f2401b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f2401b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["24-01-20",b])
for i in range(0,(len(f2401c['RESPONSE']['PEOPLE']['PERSON']))):
    c = f2401c['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["24-01-20",c])
for i in range(0,(len(f2401d['RESPONSE']['PEOPLE']['PERSON']))):
    d = f2401d['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["24-01-20",d])

#array coppie data nome per il gorno 26-01
for i in range(0,(len(f2601a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f2601a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["26-01-20",a])

#array coppie data nome per il gorno 30-01


for i in range(0,(len(f3001b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f3001b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["30-01-20",b])

#array coppie data nome per il gorno 02-02


#array coppie data nome per il gorno 03-02
for i in range(0,(len(f0302a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f0302a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["03-02-20",a])
for i in range(0,(len(f0302a['RESPONSE']['PEOPLE']['PERSON']))):
    b = f0302a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["03-02-20",b])
for i in range(0,(len(f0302a['RESPONSE']['PEOPLE']['PERSON']))):
    c = f0302a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["03-02-20",c])

#array coppie data nome per il gorno 05-02
for i in range(0,(len(f0502a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f0502a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["05-02-20",a])

#array coppie data nome per il gorno 06-02
for i in range(0,(len(f0602a['RESPONSE']['PEOPLE']['PERSON']))):
    a = f0602a['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["06-02-20",a])
for i in range(0,(len(f0602b['RESPONSE']['PEOPLE']['PERSON']))):
    b = f0602b['RESPONSE']['PEOPLE']['PERSON'][i]['BASE']
    people.append(["06-02-20",b])






 #################################################àà

with open('/home/luca/Scrivania/javascript/people.json', 'w') as f:
    f.write("{ \n \"people\" :  [\n")
    for item in people:
        f.write("       { \"date\": \"%s\"," %item[0])
        f.write(" \"name\": \"%s\"" %item[1])
        f.write("},\n")
    f.write("       ]\n")
    f.write("}\n")

print("finish")