import json
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt


#caricamento json file f+data+lettera

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


keywords = []

# per il giorn 08-11 

for i in range (0, len(f0811a['RESPONSE']['TAGGING'])):
    check_a = f0811a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_a == "MAINELEMENTS"):
        for j in range (0, len(f0811a['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_a = f0811a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_a = f0811a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_a = f0811a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["08-11-19",label_a,typ_a,score_a])
for i in range (0, len(f0811b['RESPONSE']['TAGGING'])):
    check_b = f0811a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_b == "MAINELEMENTS"):
        for j in range (0, len(f0811b['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_b = f0811b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_b = f0811b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_b = f0811b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["08-11-19",label_b,typ_b,score_b])

# per il giorn 09-11 

for i in range (0, len(f0911a['RESPONSE']['TAGGING'])):
    check_a = f0911a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_a == "MAINELEMENTS"):
        for j in range (0, len(f0911a['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_a = f0911a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_a = f0911a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_a = f0911a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["09-11-19",label_a,typ_a,score_a])

# per il giorn 11-11

for i in range (0, len(f1111a['RESPONSE']['TAGGING'])):
    check_a = f1111a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_a == "MAINELEMENTS"):
        for j in range (0, len(f1111a['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_a = f1111a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_a = f1111a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_a = f1111a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["11-11-19",label_a,typ_a,score_a])
for i in range (0, len(f1111b['RESPONSE']['TAGGING'])):
    check_b = f1111a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_b == "MAINELEMENTS"):
        for j in range (0, len(f1111b['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_b = f1111b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_b = f1111b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_b = f1111b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["11-11-19",label_b,typ_b,score_b])
# per il giorn 20-11
for i in range (0, len(f2011a['RESPONSE']['TAGGING'])):
    check_a = f2011a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_a == "MAINELEMENTS"):
        for j in range (0, len(f2011a['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_a = f2011a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_a = f2011a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_a = f2011a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["20-11-19",label_a,typ_a,score_a])
# per il giorn 21-11
for i in range (0, len(f2111a['RESPONSE']['TAGGING'])):
    check_a = f2111a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_a == "MAINELEMENTS"):
        for j in range (0, len(f2111a['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_a = f2111a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_a = f2111a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_a = f2111a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["21-11-19",label_a,typ_a,score_a])
for i in range (0, len(f2111b['RESPONSE']['TAGGING'])):
    check_b = f2111a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_b == "MAINELEMENTS"):
        for j in range (0, len(f2111b['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_b = f2111b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_b = f2111b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_b = f2111b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["21-11-19",label_b,typ_b,score_b])
# per il giorn 22-11
for i in range (0, len(f2211a['RESPONSE']['TAGGING'])):
    check_a = f2211a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_a == "MAINELEMENTS"):
        for j in range (0, len(f2211a['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_a = f2211a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_a = f2211a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_a = f2211a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["22-11-19",label_a,typ_a,score_a])
for i in range (0, len(f2211b['RESPONSE']['TAGGING'])):
    check_b = f2211a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_b == "MAINELEMENTS"):
        for j in range (0, len(f2211b['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_b = f2211b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_b = f2211b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_b = f2211b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["22-11-19",label_b,typ_b,score_b])
# per il giorn 25-11
for i in range (0, len(f2511a['RESPONSE']['TAGGING'])):
    check_a = f2511a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_a == "MAINELEMENTS"):
        for j in range (0, len(f2511a['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_a = f2511a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_a = f2511a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_a = f2511a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["25-11-19",label_a,typ_a,score_a])
for i in range (0, len(f2511b['RESPONSE']['TAGGING'])):
    check_b = f2511a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_b == "MAINELEMENTS"):
        for j in range (0, len(f2511b['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_b = f2511b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_b = f2511b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_b = f2511b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["25-11-19",label_b,typ_b,score_b])

# per il giorn 04-12

for i in range (0, len(f0412a['RESPONSE']['TAGGING'])):
    check_a = f0412a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_a == "MAINELEMENTS"):
        for j in range (0, len(f0412a['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_a = f0412a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_a = f0412a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_a = f0412a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["04-12-19",label_a,typ_a,score_a])
for i in range (0, len(f0412b['RESPONSE']['TAGGING'])):
    check_b = f0412a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_b == "MAINELEMENTS"):
        for j in range (0, len(f0412b['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_b = f0412b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_b = f0412b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_b = f0412b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["04-12-19",label_b,typ_b,score_b])
# per il giorn 09-12
for i in range (0, len(f0912a['RESPONSE']['TAGGING'])):
    check_a = f0912a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_a == "MAINELEMENTS"):
        for j in range (0, len(f0912a['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_a = f0912a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_a = f0912a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_a = f0912a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["09-12-19",label_a,typ_a,score_a])
for i in range (0, len(f0912b['RESPONSE']['TAGGING'])):
    check_b = f0912a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_b == "MAINELEMENTS"):
        for j in range (0, len(f0912b['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_b = f0912b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_b = f0912b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_b = f0912b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["09-12-19",label_b,typ_b,score_b])
# per il giorn 10-12
for i in range (0, len(f1012a['RESPONSE']['TAGGING'])):
    check_a = f1012a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_a == "MAINELEMENTS"):
        for j in range (0, len(f1012a['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_a = f1012a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_a = f1012a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_a = f1012a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["10-12-19",label_a,typ_a,score_a])

# per il giorn 12-12
for i in range (0, len(f1212a['RESPONSE']['TAGGING'])):
    check_a = f1212a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_a == "MAINELEMENTS"):
        for j in range (0, len(f1212a['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_a = f1212a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_a = f1212a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_a = f1212a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["12-12-19",label_a,typ_a,score_a])
# per il giorn 13-12
for i in range (0, len(f1312a['RESPONSE']['TAGGING'])):
    check_a = f1312a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_a == "MAINELEMENTS"):
        for j in range (0, len(f1312a['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_a = f1312a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_a = f1312a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_a = f1312a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["13-12-19",label_a,typ_a,score_a])
# per il giorn 14-12
for i in range (0, len(f1412a['RESPONSE']['TAGGING'])):
    check_a = f1412a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_a == "MAINELEMENTS"):
        for j in range (0, len(f1412a['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_a = f1412a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_a = f1412a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_a = f1412a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["14-12-19",label_a,typ_a,score_a])
# per il giorn 15-12
for i in range (0, len(f1512a['RESPONSE']['TAGGING'])):
    check_a = f1512a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_a == "MAINELEMENTS"):
        for j in range (0, len(f1512a['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_a = f1512a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_a = f1512a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_a = f1512a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["15-12-19",label_a,typ_a,score_a])
for i in range (0, len(f1512b['RESPONSE']['TAGGING'])):
    check_a = f1512b['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_a == "MAINELEMENTS"):
        for j in range (0, len(f1512b['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_a = f1512b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_a = f1512b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_a = f1512b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["15-12-19",label_a,typ_a,score_a])
# per il giorn 18-12
for i in range (0, len(f1812a['RESPONSE']['TAGGING'])):
    check_a = f1812a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_a == "MAINELEMENTS"):
        for j in range (0, len(f1812a['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_a = f1812a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_a = f1812a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_a = f1812a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["18-12-19",label_a,typ_a,score_a])
for i in range (0, len(f1812b['RESPONSE']['TAGGING'])):
    check_a = f1812b['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_a == "MAINELEMENTS"):
        for j in range (0, len(f1812b['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_a = f1812b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_a = f1812b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_a = f1812b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["18-12-19",label_a,typ_a,score_a])
# per il giorn 19-12
for i in range (0, len(f1912a['RESPONSE']['TAGGING'])):
    check_a = f1912a['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_a == "MAINELEMENTS"):
        for j in range (0, len(f1912a['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_a = f1912a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_a = f1912a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_a = f1912a['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["19-12-19",label_a,typ_a,score_a])
for i in range (0, len(f1912b['RESPONSE']['TAGGING'])):
    check_a = f1912b['RESPONSE']['TAGGING'][i]['FEATURE'] 
    if (check_a == "MAINELEMENTS"):
        for j in range (0, len(f1912b['RESPONSE']['TAGGING'][i]["LEMMA"])):
            label_a = f1912b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["LABEL"]
            typ_a = f1912b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["TYPE"]
            score_a = f1912b['RESPONSE']['TAGGING'][i]["LEMMA"][j]["SCORE"]
            keywords.append(["19-12-19",label_a,typ_a,score_a])


#with open('/home/luca/Scrivania/javascript/keywords.txt', 'w') as f:
   # for item in keywords:
    #    f.write("%s," % item)

with open('/home/luca/Scrivania/javascript/keyWord/kW.json', 'w') as f:
    f.write("{ \n \"keyword\" :  [\n")
    for item in keywords:
        f.write("       { \"date\": \"%s\"," %item[0])
        f.write(" \"entity\": \"%s\"," %item[1])
        f.write(" \"type\": \"%s\"," %item[2])
        f.write(" \"frequency\": \"%s\"" %item[3])
        f.write("},\n")
    f.write("       ]\n")
    f.write("}\n")

