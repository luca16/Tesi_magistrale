import json
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import caricamento
from caricamento import *

adiacenza = []


#26-09 
for i in range(0,len(f2609a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2609a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2609a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["26-09-19",node,idnode])


#8-10 
for i in range(0,len(f0810a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0810a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0810a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["08-10-19",node,idnode])
for i in range(0,len(f0810b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0810b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0810b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["08-10-19",node,idnode])

#11-10 
for i in range(0,len(f1110a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1110a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1110a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["11-10-19",node,idnode])

#14-10 
for i in range(0,len(f1410a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1410a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1410a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["14-10-19",node,idnode])
for i in range(0,len(f1410b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1410b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1410b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["14-10-19",node,idnode])

#22-10 
for i in range(0,len(f2210a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2210a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2210a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["22-10-19",node,idnode])
for i in range(0,len(f2210b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2210b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2210b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["22-10-19",node,idnode])

#31-10
for i in range(0,len(f3110a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f3110a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f3110a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["31-10-19",node,idnode])
for i in range(0,len(f3110b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f3110b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f3110b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["31-10-19",node,idnode])

#8-11 
for i in range(0,len(f0811a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0811a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0811a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["08-11-19",node,idnode])
for i in range(0,len(f0811b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0811b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0811b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["08-11-19",node,idnode])

#09-11
for i in range(0,len(f0911a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0911a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0911a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["09-11-19",node,idnode])

#11-11 
for i in range(0,len(f1111a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1111a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1111a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["11-11-19",node,idnode])
for i in range(0,len(f1111b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1111b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1111b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["11-11-19",node,idnode])

#14-11 
for i in range(0,len(f1411a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1411a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1411a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["14-11-19",node,idnode])

#15-11 
for i in range(0,len(f1511a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1511a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1511a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["15-11-19",node,idnode])
for i in range(0,len(f1511b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1511b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1511b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["15-11-19",node,idnode])


#19-11 
for i in range(0,len(f1911a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1911a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1911a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["19-11-19",node,idnode])

#20-11 
for i in range(0,len(f2011a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2011a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2011a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["20-11-19",node,idnode])


#21-11 
for i in range(0,len(f2111a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2111a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2111a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["21-11-19",node,idnode])
for i in range(0,len(f2111b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2111b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2111b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["21-11-19",node,idnode])
for i in range(0,len(f2111c["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2111c["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2111c["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["21-11-19",node,idnode])

#22-11 
for i in range(0,len(f2211a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2211a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2211a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["22-11-19",node,idnode])
for i in range(0,len(f2211b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2211b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2211b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["22-11-19",node,idnode])

#25-11 
for i in range(0,len(f2511a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2511a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2511a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["25-11-19",node,idnode])
for i in range(0,len(f2511b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2511b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2511b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["25-11-19",node,idnode])

#26-11
for i in range(0,len(f2611b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2611b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2611b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["26-11-19",node,idnode])

#04-12 
for i in range(0,len(f0412a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0412a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0412a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["04-12-19",node,idnode])
for i in range(0,len(f0412b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0412b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0412b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["04-12-19",node,idnode])

#09-12 
for i in range(0,len(f0912a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0912a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0912a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["09-12-19",node,idnode])
for i in range(0,len(f0912b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0912b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0912b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["09-12-19",node,idnode])

#10-12 
for i in range(0,len(f1012a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1012a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1012a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["10-12-19",node,idnode])

#12-12 
for i in range(0,len(f1212a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1212a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1212a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["12-12-19",node,idnode])


#13-12 
for i in range(0,len(f1312a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1312a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1312a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["13-12-19",node,idnode])


#14-12 
for i in range(0,len(f1412a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1412a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1412a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["14-12-19",node,idnode])

#15-12 
for i in range(0,len(f1512a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1512a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1512a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["15-12-19",node,idnode])
for i in range(0,len(f1512b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1512b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1512b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["15-12-19",node,idnode])

#18-12 
for i in range(0,len(f1812a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1812a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1812a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["18-12-19",node,idnode])
for i in range(0,len(f1812b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1812b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1812b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["18-12-19",node,idnode])


#19-12 
for i in range(0,len(f1912a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1912a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1912a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["19-12-19",node,idnode])
for i in range(0,len(f1912b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f1912b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f1912b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["19-12-19",node,idnode])

#21-01 
for i in range(0,len(f2101a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2101a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2101a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["21-01-20",node,idnode])

#22-01 
for i in range(0,len(f2201a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2201a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2201a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["22-01-20",node,idnode])
for i in range(0,len(f2201b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2201b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2201b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["22-01-20",node,idnode])
for i in range(0,len(f2201c["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2201c["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2201c["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["22-01-20",node,idnode])
for i in range(0,len(f2201d["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2201d["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2201d["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["22-01-20",node,idnode])
for i in range(0,len(f2201e["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2201e["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2201e["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["22-01-20",node,idnode])

#23-01 
for i in range(0,len(f2301a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2301a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2301a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["23-01-20",node,idnode])
for i in range(0,len(f2301b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2301b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2301b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["23-01-20",node,idnode])
for i in range(0,len(f2301c["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2301c["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2301c["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["23-01-20",node,idnode])
for i in range(0,len(f2301d["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2301d["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2301d["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["23-01-20",node,idnode])

#24-01 
for i in range(0,len(f2401a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2401a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2401a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["24-01-20",node,idnode])
for i in range(0,len(f2401b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2401b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2401b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["24-01-20",node,idnode])
for i in range(0,len(f2401c["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2401c["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2401c["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["24-01-20",node,idnode])
for i in range(0,len(f2401d["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2401d["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2401d["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["24-01-20",node,idnode])


#26-01 
for i in range(0,len(f2601a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f2601a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f2601a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["26-01-20",node,idnode])

#30-01 
for i in range(0,len(f3001a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f3001a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f3001a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["30-01-20",node,idnode])
for i in range(0,len(f3001b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f3001b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f3001b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["30-01-20",node,idnode])




#03-02 
for i in range(0,len(f0302a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0302a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0302a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["03-02-20",node,idnode])
for i in range(0,len(f0302b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0302b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0302b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["03-02-20",node,idnode])
for i in range(0,len(f0302c["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0302c["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0302c["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["03-02-20",node,idnode])

#05-02 
for i in range(0,len(f0502a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0502a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0502a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["05-02-20",node,idnode])

#06-02 
for i in range(0,len(f0602a["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0602a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0602a["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["06-02-20",node,idnode])
for i in range(0,len(f0602b["RESPONSE"]["TEXTMINING"][3]['NODES']['NODE'])):
    node = f0602b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["content"]
    idnode = f0602b["RESPONSE"]["TEXTMINING"][3]['NODES']["NODE"][i]["ID"]
    adiacenza.append(["06-02-20",node,idnode])






relations = []

#26-09
for i in range(0,len(f2609a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2609a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2609a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2609a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["26-09-19",s,t,typ])

#08-10 
for i in range(0,len(f0810a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0810a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0810a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0810a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["08-10-19",s,t,typ])

for i in range(0,len(f0810b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0810b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0810b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0810b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["08-10-19",s,t,typ]) 

#11-10 
for i in range(0,len(f1110a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1110a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1110a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1110a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["11-10-19",s,t,typ])



#14-10 
for i in range(0,len(f1410a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1410a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1410a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1410a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["14-10-19",s,t,typ])

for i in range(0,len(f1410b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1410b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1410b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1410b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["14-10-19",s,t,typ])

#22-10 
for i in range(0,len(f2210a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2210a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2210a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2210a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["22-10-19",s,t,typ])

for i in range(0,len(f2210b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2210b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2210b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2210b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["22-10-19",s,t,typ]) 

#31-10 
for i in range(0,len(f3110a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f3110a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f3110a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f3110a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["31-10-19",s,t,typ])

for i in range(0,len(f3110b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f3110b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f3110b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f3110b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["31-10-19",s,t,typ]) 

#8-11 
for i in range(0,len(f0811a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0811a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0811a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0811a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["08-11-19",s,t,typ])

for i in range(0,len(f0811b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0811b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0811b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0811b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["08-11-19",s,t,typ])

#9-11 
for i in range(0,len(f0911a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0911a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0911a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0911a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["09-11-19",s,t,typ])

#11-11 
for i in range(0,len(f1111a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1111a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1111a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1111a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["11-11-19",s,t,typ])

for i in range(0,len(f1111b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1111b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1111b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1111b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["11-11-19",s,t,typ])


#14-11 
for i in range(0,len(f1411a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1411a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1411a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1411a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["14-11-19",s,t,typ])

#15-11 
for i in range(0,len(f1511a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1511a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1511a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1511a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["15-11-19",s,t,typ])

for i in range(0,len(f1511b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1511b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1511b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1511b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["15-11-19",s,t,typ])

#19-11 
for i in range(0,len(f1911a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1911a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1911a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1911a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["19-11-19",s,t,typ])

#20-11 
for i in range(0,len(f2011a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2011a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2011a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2011a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["20-11-19",s,t,typ])


#21-11 
for i in range(0,len(f2111a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2111a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2111a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2111a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["21-11-19",s,t,typ])

for i in range(0,len(f2111b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2111b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2111b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2111b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["21-11-19",s,t,typ])

for i in range(0,len(f2111c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2111c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2111c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2111c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["21-11-19",s,t,typ])

#22-11 
for i in range(0,len(f2211a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2211a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2211a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2211a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["22-11-19",s,t,typ])

for i in range(0,len(f2211b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2211b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2211b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2211b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["22-11-19",s,t,typ])

#25-11 
for i in range(0,len(f2511a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2511a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2511a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2511a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["25-11-19",s,t,typ])

for i in range(0,len(f2511b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2511b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2511b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2511b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["25-11-19",s,t,typ])

#26-11
for i in range(0,len(f2611b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2611b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2611b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2611b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["26-11-19",s,t,typ])


#04-12 
for i in range(0,len(f0412a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0412a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0412a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0412a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["04-12-19",s,t,typ])

for i in range(0,len(f0412b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0412b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0412b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0412b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["04-12-19",s,t,typ])

#09-12
for i in range(0,len(f0912a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0912a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0912a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0912a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["09-12-19",s,t,typ])

for i in range(0,len(f0912b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0912b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0912b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0912b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["09-12-19",s,t,typ])

#10-12
for i in range(0,len(f1012a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1012a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1012a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1012a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["10-12-19",s,t,typ])


    
#12-12 
for i in range(0,len(f1212a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1212a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1212a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1212a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["12-12-19",s,t,typ])

#13-12
for i in range(0,len(f1312a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1312a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1312a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1312a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["13-12-19",s,t,typ])

#14-12
for i in range(0,len(f1412a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1412a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1412a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1412a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["14-12-19",s,t,typ])

#15-12
for i in range(0,len(f1512a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1512a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1512a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1512a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["15-12-19",s,t,typ])

for i in range(0,len(f1512b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1512b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1512b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1512b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["15-12-19",s,t,typ])

#18-12
for i in range(0,len(f1812a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1812a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1812a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1812a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["18-12-19",s,t,typ])

for i in range(0,len(f1812b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1812b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1812b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1812b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["18-12-19",s,t,typ])

#19-12
for i in range(0,len(f1912a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1912a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1912a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1912a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["19-12-19",s,t,typ])

for i in range(0,len(f1912b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f1912b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f1912b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f1912b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["19-12-19",s,t,typ])

#21-01
for i in range(0,len(f2101a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2101a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2101a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2101a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["21-01-20",s,t,typ])


#22-01
for i in range(0,len(f2201a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2201a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2201a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2201a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["22-01-20",s,t,typ])
for i in range(0,len(f2201b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2201b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2201b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2201b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["22-01-20",s,t,typ])
for i in range(0,len(f2201c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2201c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2201c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2201c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["22-01-20",s,t,typ])
for i in range(0,len(f2201d["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2201d["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2201d["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2201d["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["22-01-20",s,t,typ])
for i in range(0,len(f2201e["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2201e["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2201e["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2201e["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["22-01-20",s,t,typ])



#23-01
for i in range(0,len(f2301a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2301a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2301a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2301a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["23-01-20",s,t,typ])
for i in range(0,len(f2301b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2301b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2301b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2301b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["23-01-20",s,t,typ])
for i in range(0,len(f2301c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2301c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2301c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2301c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["23-01-20",s,t,typ])
for i in range(0,len(f2301d["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2301d["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2301d["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2301d["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["23-01-20",s,t,typ])

#24-01
for i in range(0,len(f2401a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2401a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2401a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2401a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["24-01-20",s,t,typ])
for i in range(0,len(f2401b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2401b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2401b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2401b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["24-01-20",s,t,typ])
for i in range(0,len(f2401c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2401c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2401c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2401c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["24-01-20",s,t,typ])
for i in range(0,len(f2401d["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2401d["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2401d["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2401d["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["24-01-20",s,t,typ])

#26-01
for i in range(0,len(f2601a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f2601a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f2601a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f2601a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["26-01-20",s,t,typ])


#30-01
for i in range(0,len(f3001a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f3001a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f3001a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f3001a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["30-01-20",s,t,typ])
for i in range(0,len(f3001b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f3001b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f3001b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f3001b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["30-01-20",s,t,typ])




#03-02
for i in range(0,len(f0302a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0302a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0302a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0302a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["03-02-20",s,t,typ])
for i in range(0,len(f0302b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0302b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0302b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0302b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["03-02-20",s,t,typ])
for i in range(0,len(f0302c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0302c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0302c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0302c["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["03-02-20",s,t,typ])

#05-02
for i in range(0,len(f0502a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0502a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0502a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0502a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["05-02-20",s,t,typ])

#06-02
for i in range(0,len(f0602a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0602a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0602a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0602a["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["06-02-20",s,t,typ])
for i in range(0,len(f0602b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"])):
    s = f0602b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["SOURCE"]
    t = f0602b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TARGET"]
    typ = f0602b["RESPONSE"]["TEXTMINING"][3]["RELATIONS"]["REL"][i]["TYPE"]
    relations.append(["06-02-20",s,t,typ])






#with open('/home/luca/Scrivania/javascript/adiacenza.txt', 'w') as f:
 #   for item in adiacenza:
  #      f.write("%s," % item)

#with open('/home/luca/Scrivania/javascript/relations.txt', 'w') as f:
 #   for item in relations:
  #      f.write("%s," % item)

out = []
adi = adiacenza
def getName(data,ident):
    for a in adiacenza:
        if (a[0]==data):
            if(a[2]==ident):
                return a[1]


for r in relations: 
        out.append([r[0],getName(r[0],r[1]),getName(r[0],r[2]),r[3]])



with open('/home/luca/Scrivania/javascript/a.json', 'w') as f:
    f.write("{ \n \"nodes\" :  [\n")
    for item in adiacenza:
        f.write("       { \"date\": \"%s\"," %item[0])
        f.write(" \"name\": \"%s\"," %item[1])
        f.write(" \"id\": \"%s\"" %item[2])
        f.write("},\n")
    f.write("       ]\n")
    f.write("}\n")

with open('/home/luca/Scrivania/javascript/r.json', 'w') as f:
    f.write("{ \n \"links\" :  [\n")
    for item in out:
        f.write("       { \"date\": \"%s\"," %item[0])
        f.write(" \"source\": \"%s\"," %item[1])
        f.write(" \"target\": \"%s\"," %item[2])
        f.write(" \"type\": \"%s\" " %item[3])
        f.write("},\n")
    f.write("       ]\n")
    f.write("}\n")
