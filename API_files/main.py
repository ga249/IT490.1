#!/usr/bin/env python3

import apiCalls
import jsonParser
import json
import subprocess
import time

if (apiCalls.grabMenShirts()):
    subprocess.call(["php","-f","../publishLog.php","shirts grabbed"])
    idList = jsonParser.getPIDfromJson("MenShirtApiData.json")
    if len(idList) != 20:
        subprocess.call(["php","-f","../publishLog.php","error main: idList not 20"])
        print('error main: idList not 20')
        
    
    print(idList)
    prodDict = apiCalls.grabDetails(idList, "male")
    if prodDict == False:
        subprocess.call(["php","-f","../publishLog.php","error main:19 grabDetails failed"])
        print('error main: grabDetails failed')
        exit()
    f = open('MenShirtsReady.json', 'w')
    json.dump(prodDict, f)
    time.sleep(1)
    subprocess.call(["php","-f","../dmzToWeb.php","MenShirtsReady.json"])

if (apiCalls.grabWomenTops()):
    subprocess.call(["php","-f","../publishLog.php","tops grabbed"])
    idList = jsonParser.getPIDfromJson("WomenTopsApiData.json")
    if len(idList) != 20:
        subprocess.call(["php","-f","../publishLog.php","error main: idList not 20"])
        print('error main: idList not 20')
        
    
    print(idList)
    prodDict = apiCalls.grabDetails(idList, "female")
    if prodDict == False:
        subprocess.call(["php","-f","../publishLog.php","error main:36 grabDetails failed"])
        print('error main: grabDetails failed')
        
    f = open('WomenTopsReady.json', 'w')
    json.dump(prodDict, f)
    time.sleep(1)
    subprocess.call(["php","-f","../dmzToWeb.php","WomenTopsReady.json"])

