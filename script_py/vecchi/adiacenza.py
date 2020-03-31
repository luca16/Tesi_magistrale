import json
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import caricamento
from caricamento import *


adiacenza = []

#8-11 
for i in range(0,len(f0811a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0811a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0811a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[0],node,idnode])
for i in range(0,len(f0811b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0811b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0811b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[0],node,idnode])

#09-11
for i in range(0,len(f0911a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0911a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0911a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[1],node,idnode])

#11-11 
for i in range(0,len(f1111a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1111a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1111a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[2],node,idnode])
for i in range(0,len(f1111b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1111b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1111b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[2],node,idnode])

#20-11 
for i in range(0,len(f2011a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2011a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2011a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[3],node,idnode])


#21-11 
for i in range(0,len(f2111a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2111a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2111a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[4],node,idnode])
for i in range(0,len(f2111b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2111b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2111b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[4],node,idnode])
for i in range(0,len(f2111c["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2111c["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2111c["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[4],node,idnode])

#22-11 
for i in range(0,len(f2211a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2211a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2211a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[5],node,idnode])
for i in range(0,len(f2211b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2211b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2211b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[5],node,idnode])

#25-11 
for i in range(0,len(f2511a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2511a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2511a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[6],node,idnode])
for i in range(0,len(f2511b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2511b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2511b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[6],node,idnode])

#04-12 
for i in range(0,len(f0412a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0412a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0412a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[7],node,idnode])
for i in range(0,len(f0412b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0412b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0412b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[7],node,idnode])

#09-12 
for i in range(0,len(f0912a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0912a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0912a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[8],node,idnode])
for i in range(0,len(f0912b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0912b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0912b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[8],node,idnode])

#10-12 
for i in range(0,len(f1012a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1012a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1012a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[9],node,idnode])

#12-12 
for i in range(0,len(f1212a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1212a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1212a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[10],node,idnode])


#13-12 
for i in range(0,len(f1312a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1312a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1312a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[11],node,idnode])


#14-12 
for i in range(0,len(f1412a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1412a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1412a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[12],node,idnode])

#15-12 
for i in range(0,len(f1512a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1512a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1512a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[13],node,idnode])
for i in range(0,len(f1512b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1512b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1512b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[13],node,idnode])

#18-12 
for i in range(0,len(f1812a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1812a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1812a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[14],node,idnode])
for i in range(0,len(f1812b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1812b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1812b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[14],node,idnode])


#19-12 
for i in range(0,len(f1912a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1912a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1912a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[15],node,idnode])
for i in range(0,len(f1912b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1912b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1912b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append([date[15],node,idnode])




relations = []




#8-11 
for i in range(0,len(f0811a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0811a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0811a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0811a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[0],s,t,typ])

for i in range(0,len(f0811b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0811b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0811b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0811b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[0],s,t,typ])


#9-11 
for i in range(0,len(f0911a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0911a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0911a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0911a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[1],s,t,typ])

#11-11 
for i in range(0,len(f1111a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1111a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1111a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1111a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[2],s,t,typ])

for i in range(0,len(f1111b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1111b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1111b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1111b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[2],s,t,typ])

#20-11 
for i in range(0,len(f2011a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2011a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2011a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2011a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[3],s,t,typ])


#21-11 
for i in range(0,len(f2111a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2111a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2111a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2111a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[4],s,t,typ])

for i in range(0,len(f2111b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2111b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2111b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2111b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[4],s,t,typ])

for i in range(0,len(f2111c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2111c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2111c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2111c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[4],s,t,typ])

#22-11 
for i in range(0,len(f2211a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2211a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2211a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2211a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[5],s,t,typ])

for i in range(0,len(f2211b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2211b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2211b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2211b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[5],s,t,typ])

#25-11 
for i in range(0,len(f2511a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2511a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2511a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2511a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[6],s,t,typ])

for i in range(0,len(f2511b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2511b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2511b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2511b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[6],s,t,typ])

#04-12 
for i in range(0,len(f0412a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0412a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0412a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0412a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[7],s,t,typ])

for i in range(0,len(f0412b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0412b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0412b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0412b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[7],s,t,typ])

#09-12
for i in range(0,len(f0912a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0912a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0912a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0912a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[8],s,t,typ])

for i in range(0,len(f0912b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0912b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0912b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0912b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[8],s,t,typ])

#10-12
for i in range(0,len(f1012a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1012a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1012a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1012a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[9],s,t,typ])


    
#12-12 
for i in range(0,len(f1212a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1212a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1212a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1212a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[10],s,t,typ])

#13-12
for i in range(0,len(f1312a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1312a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1312a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1312a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[11],s,t,typ])

#14-12
for i in range(0,len(f1412a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1412a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1412a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1412a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[12],s,t,typ])

#15-12
for i in range(0,len(f1512a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1512a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1512a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1512a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[13],s,t,typ])

for i in range(0,len(f1512b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1512b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1512b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1512b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[13],s,t,typ])

#18-12
for i in range(0,len(f1812a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1812a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1812a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1812a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[14],s,t,typ])

for i in range(0,len(f1812b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1812b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1812b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1812b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[14],s,t,typ])

#19-12
for i in range(0,len(f1912a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1912a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1912a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1912a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[15],s,t,typ])

for i in range(0,len(f1912b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1912b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1912b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1912b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append([date[15],s,t,typ])


#with open('/home/luca/Scrivania/javascript/adiacenza.txt', 'w') as f:
 #   for item in adiacenza:
  #      f.write("%s," % item)

#with open('/home/luca/Scrivania/javascript/relations.txt', 'w') as f:
 #   for item in relations:
  #      f.write("%s," % item)

with open('/home/luca/Scrivania/javascript/adiacenza.json', 'w') as f:
    f.write("{ \n \"nodes\" :  [\n")
    for item in adiacenza:
        f.write("       { \"date\": \"%s\"," %item[0])
        f.write(" \"name\": \"%s\"," %item[1])
        f.write(" \"id\": \"%s" %item[0])
        f.write("-%s\"" %item[2])
        f.write("},\n")
    f.write("       ]\n")
    f.write("}\n")

with open('/home/luca/Scrivania/javascript/relations.json', 'w') as f:
    f.write("{ \n \"links\" :  [\n")
    for item in relations:
        f.write("       { \"date\": \"%s\"," %item[0])
        f.write(" \"source\": \"%s" %item[0])
        f.write("-%s\"," %item[1])
        f.write(" \"target\": \"%s" %item[0])
        f.write("-%s\"," %item[2])
        f.write(" \"type\": \"%s\" " %item[2])
        f.write("},\n")
    f.write("       ]\n")
    f.write("}\n")