import json
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

# array di date
date = ["26-09-19","08-10-19","11-10-19","14-10-19","22-10-19","31-10-19","08-11-19","09-11-19","11-11-19","14-11-19","15-11-19","19-11-19","20-11-19","21-11-19","22-11-19","25-11-19","26-11-19","04-12-19","09-12-19","10-12-19","13-12-19","14-12-19","15-12-19","18-12-19","19-12-19","21-01-20","22-01-20","23-01-20","24-01-20","26-01-20","30-01-20","02-02-20","03-02-20","05-02-20","06-02-20"]

#caricamento json file f+data+lettera

with open('/home/luca/Scrivania/javascript/jsonfile/26-09-19a.json') as json_file:
    f2609a = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/08-10-19a.json') as json_file:
    f0810a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/08-10-19b.json') as json_file:
    f0810b = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/11-10-19a.json') as json_file:
    f1110a = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/14-10-19a.json') as json_file:
    f1410a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/14-10-19b.json') as json_file:
    f1410b = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/22-10-19a.json') as json_file:
    f2210a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/22-10-19b.json') as json_file:
    f2210b = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/31-10-19a.json') as json_file:
    f3110a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/31-10-19b.json') as json_file:
    f3110b = json.load(json_file)
    json_file.close()

#########################

with open('/home/luca/Scrivania/javascript/jsonfile/08-11-19a.json') as json_file:
    f0811a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/08-11-19b.json') as json_file:
    f0811b = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/09-11-19a.json') as json_file:
    f0911a = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/11-11-19a.json') as json_file:
    f1111a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/11-11-19b.json') as json_file:
    f1111b = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/14-11-19a.json') as json_file:
    f1411a = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/15-11-19a.json') as json_file:
    f1511a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/15-11-19b.json') as json_file:
    f1511b = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/19-11-19a.json') as json_file:
    f1911a = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/20-11-19a.json') as json_file:
    f2011a = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/21-11-19a.json') as json_file:
    f2111a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/21-11-19b.json') as json_file:
    f2111b = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/21-11-19c.json') as json_file:
    f2111c = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/22-11-19a.json') as json_file:
    f2211a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/22-11-19b.json') as json_file:
    f2211b = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/25-11-19a.json') as json_file:
    f2511a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/25-11-19b.json') as json_file:
    f2511b = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/26-11-19b.json') as json_file:
    f2611b = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/04-12-19a.json') as json_file:
    f0412a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/04-12-19b.json') as json_file:
    f0412b = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/09-12-19a.json') as json_file:
    f0912a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/09-12-19b.json') as json_file:
    f0912b = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/10-12-19a.json') as json_file:
    f1012a = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/12-12-19a.json') as json_file:
    f1212a = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/13-12-19a.json') as json_file:
    f1312a = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/14-12-19a.json') as json_file:
    f1412a = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/15-12-19a.json') as json_file:
    f1512a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/15-12-19b.json') as json_file:
    f1512b = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/18-12-19a.json') as json_file:
    f1812a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/18-12-19b.json') as json_file:
    f1812b = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/19-12-19a.json') as json_file:
    f1912a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/19-12-19b.json') as json_file:
    f1912b = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/21-01-20a.json') as json_file:
    f2101a = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/22-01-20a.json') as json_file:
    f2201a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/22-01-20b.json') as json_file:
    f2201b = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/22-01-20c.json') as json_file:
    f2201c = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/22-01-20d.json') as json_file:
    f2201d = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/22-01-20e.json') as json_file:
    f2201e = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/23-01-20a.json') as json_file:
    f2301a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/23-01-20b.json') as json_file:
    f2301b = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/23-01-20c.json') as json_file:
    f2301c = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/23-01-20d.json') as json_file:
    f2301d = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/24-01-20a.json') as json_file:
    f2401a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/24-01-20b.json') as json_file:
    f2401b = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/24-01-20c.json') as json_file:
    f2401c = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/24-01-20d.json') as json_file:
    f2401d = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/26-01-20a.json') as json_file:
    f2601a = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/30-01-20a.json') as json_file:
    f3001a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/30-01-20b.json') as json_file:
    f3001b = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/02-02-20a.json') as json_file:
    f0202a = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/03-02-20a.json') as json_file:
    f0302a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/03-02-20b.json') as json_file:
    f0302b = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/03-02-20c.json') as json_file:
    f0302c = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/05-02-20a.json') as json_file:
    f0502a = json.load(json_file)
    json_file.close()

with open('/home/luca/Scrivania/javascript/jsonfile/06-02-20a.json') as json_file:
    f0602a = json.load(json_file)
    json_file.close()
with open('/home/luca/Scrivania/javascript/jsonfile/06-02-20b.json') as json_file:
    f0602b = json.load(json_file)
    json_file.close()