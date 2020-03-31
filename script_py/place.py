import json
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import caricamento
from caricamento import *

####  dati geografici ################à

geoData = []

#array coppie data paesi per il gorno 26-09
for i in range(0,len(f2609a['RESPONSE']['FACTMINING'][3]['DOMAIN'])):
    a = f2609a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["26-09-19",a])

#array coppie data paesi per il gorno 08-10
for i in range(0,len(f0810a['RESPONSE']['FACTMINING'][3]['DOMAIN'])):
    a = f0810a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["08-10-19",a])
for i in range(0,len(f0810a['RESPONSE']['FACTMINING'][3]['DOMAIN'])):
    b = f0810b['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["08-10-19",b])

#array coppie data paesi per il gorno 11-10
for i in range(0,len(f1110a['RESPONSE']['FACTMINING'][3]['DOMAIN'])):
    a = f1110a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["11-10-19",a])


#array coppie data paesi per il gorno 14-10

    a = f1410a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["14-10-19",a])

    b = f1410b['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["14-10-19",b])

#array coppie data paesi per il gorno 22-10
for i in range(0,len(f2210a['RESPONSE']['FACTMINING'][3]['DOMAIN'])):
    a = f2210a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["22-10-19",a])
for i in range(0,len(f2210b['RESPONSE']['FACTMINING'][3]['DOMAIN'])):
    b = f2210b['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["22-10-19",b])

#array coppie data paesi per il gorno 31-10

    
for i in range(0,len(f3110b['RESPONSE']['FACTMINING'][3]['DOMAIN'])):
    b = f3110b['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["31-10-19",b])

#array coppie data paesi per il gorno 08-11
for i in range(0,len(f0811a['RESPONSE']['FACTMINING'][3]['DOMAIN'])):
    a = f0811a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["08-11-19",a])
for i in range(0,len(f0811a['RESPONSE']['FACTMINING'][3]['DOMAIN'])):
    b = f0811b['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["08-11-19",b])

for i in range(0,len(f0911a['RESPONSE']['FACTMINING'][3]['DOMAIN'])):
    a = f0911a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["09-11-19",a])

#array coppie data paesi per il gorno 11-11
for i in range(0,(len(f1111a['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    a = f1111a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["11-11-19",a])
for i in range(0,(len(f1111b['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    b = f1111b['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["11-11-19",b])

#array coppie data paesi per il gorno 14-11
for i in range(0,(len(f1411a['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    a = f1411a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["14-11-19",a])

#array coppie data paesi per il gorno 15-11
for i in range(0,(len(f1511a['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    a = f1511a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["15-11-19",a])
for i in range(0,(len(f1511b['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    b = f1511b['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["15-11-19",b])

#array coppie data paesi per il gorno 19-11
for i in range(0,(len(f1911a['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    a = f1911a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["19-11-19",a])


#array coppie data nome per il gorno 20-11
for i in range(0,(len(f2011a['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    a = f2011a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["20-11-19",a])

#array coppie data nome per il gorno 21-11
for i in range(0,(len(f2111a['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    a = f2111a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["21-11-19",a])
for i in range(0,(len(f2111b['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    b = f2111b['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["21-11-19",b])
for i in range(0,(len(f2111c['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    c = f2111c['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["21-11-19",c])

#array coppie data nome per il gorno 22-11
for i in range(0,(len(f2211a['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    a = f2211a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["22-11-19",a])
for i in range(0,(len(f2211b['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    b = f2211b['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["22-11-19",b])

#array coppie data nome per il gorno 25-11
for i in range(0,(len(f2511a['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    a = f2511a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["25-11-19",a])
for i in range(0,(len(f2511b['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    b = f2511b['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["25-11-19",b])



#array coppie data nome per il gorno 04-12
    a = f0412a['RESPONSE']['FACTMINING'][3]['DOMAIN']["NAME"]
    geoData.append(["04-12-19",a])
    b = f0412b['RESPONSE']['FACTMINING'][3]['DOMAIN']["NAME"]
    geoData.append(["04-12-19",b])

#array coppie data nome per il gorno 09-12
    a = f0912a['RESPONSE']['FACTMINING'][3]['DOMAIN']["NAME"]
    geoData.append(["09-12-19",a])
for i in range(0,(len(f0912b['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    b = f0912b['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["09-12-19",b])

#array coppie data nome per il gorno 10-12

    a = f1012a['RESPONSE']['FACTMINING'][3]['DOMAIN']["NAME"]
    geoData.append(["10-12-19",a])

#array coppie data nome per il gorno 13-12
for i in range(0,(len(f1312a['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    a = f1312a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["13-12-19",a])

for i in range(0,(len(f1412a['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    a = f1412a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["14-12-19",a])

#array coppie data nome per il gorno 15-12
for i in range(0,(len(f1512a['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    a = f1512a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["15-12-19",a])

    b = f1512b['RESPONSE']['FACTMINING'][3]['DOMAIN']["NAME"]
    geoData.append(["15-12-19",b])

#array coppie data nome per il gorno 18-12
for i in range(0,(len(f1812a['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    a = f1812a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["18-12-19",a])
for i in range(0,(len(f1812b['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    b = f1812b['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["18-12-19",b])


#array coppie data nome per il gorno 19-12
    a = f1912a['RESPONSE']['FACTMINING'][3]['DOMAIN']["NAME"]
    geoData.append(["19-12-19",a])
    b = f1912b['RESPONSE']['FACTMINING'][3]['DOMAIN']["NAME"]
    geoData.append(["19-12-19",b])

#array coppie data paesi per il gorno 21-01
for i in range(0,(len(f2101a['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    a = f2101a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["21-01-19",a])

#array coppie data paesi per il gorno 22-01
for i in range(0,(len(f2201a['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    a = f2201a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["22-01-20",a])
for i in range(0,(len(f2201d['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    d = f2201d['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["22-01-20",d])
for i in range(0,(len(f2201e['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    e = f2201e['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["22-01-20",e])

#array coppie data paesi per il gorno 23-01
for i in range(0,(len(f2301a['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    a = f2301a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["23-01-20",a])

   
for i in range(0,(len(f2301c['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    c = f2301c['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["23-01-20",c])
for i in range(0,(len(f2301d['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    d = f2301d['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["23-01-20",d])

#array coppie data paesi per il gorno 24-01
for i in range(0,(len(f2401a['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    a = f2401a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["24-01-20",a])


for i in range(0,(len(f2401d['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    d = f2401d['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["24-01-20",d])

#array coppie data paesi per il gorno 26-01
for i in range(0,(len(f2601a['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    a = f2601a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["26-01-20",a])



#array coppie data paesi per il gorno 05-02
for i in range(0,(len(f0302a['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    a = f0302a['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["03-02-20",a])
for i in range(0,(len(f0302b['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    b = f0302b['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["03-02-20",b])
for i in range(0,(len(f0302c['RESPONSE']['FACTMINING'][3]['DOMAIN']))):
    c = f0302c['RESPONSE']['FACTMINING'][3]['DOMAIN'][i]["NAME"]
    geoData.append(["03-02-20",c])



#array coppie data paesi per il gorno 06-02


#create json file

with open('/home/luca/Scrivania/javascript/place.json', 'w') as f:
    f.write("{ \n \"geoData\" :  [\n")
    for item in geoData:
        f.write("       { \"date\": \"%s\"," %item[0])
        f.write(" \"name\": \"%s\"" %item[1])
        f.write("},\n")
    f.write("       ]\n")
    f.write("}\n")

