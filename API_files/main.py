#!/usr/bin/env python3

import apiCalls
import jsonParser
import json
import subprocess

#--------MENS TOPS---------
if (apiCalls.grabMenShirts()):
    subprocess.call(["php","-f","../publishLog.php","Mens shirts grabbed"])
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
    f.close()
    subprocess.call(["php","-f","../dmzToWeb.php","MenShirtsReady.json"])
#--------WOMENS TOPS---------
if (apiCalls.grabWomenTops()):
    subprocess.call(["php","-f","../publishLog.php","Women tops grabbed"])
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
    f.close()
    subprocess.call(["php","-f","../dmzToWeb.php","WomenTopsReady.json"])

if (apiCalls.grabMensPants()):
    subprocess.call(["php","-f","../publishLog.php","Mens pants grabbed"])
    idList = jsonParser.getPIDfromJson("MenPantsApiData.json")
    if len(idList) != 20:
        subprocess.call(["php","-f","../publishLog.php","error main: idList not 20"])
        print('error main: idList not 20')
        
    
    print(idList)
    prodDict = apiCalls.grabDetails(idList, "male")
    if prodDict == False:
        subprocess.call(["php","-f","../publishLog.php","error main:56 grabDetails failed"])
        print('error main: grabDetails failed')
        
    f = open('MenPantsReady.json', 'w')
    json.dump(prodDict, f)
    f.close()
    subprocess.call(["php","-f","../dmzToWeb.php","MenPantsReady.json"])

if (apiCalls.grabWomenBottoms()):
    subprocess.call(["php","-f","../publishLog.php","Womens bottoms grabbed"])
    idList = jsonParser.getPIDfromJson("WomenBottomApiData.json")
    if len(idList) != 20:
        subprocess.call(["php","-f","../publishLog.php","error main: idList not 20"])
        print('error main: idList not 20')
        
    
    print(idList)
    prodDict = apiCalls.grabDetails(idList, "male")
    if prodDict == False:
        subprocess.call(["php","-f","../publishLog.php","error main:77 grabDetails failed"])
        print('error main: grabDetails failed')
        
    f = open('WomenBottomsReady.json', 'w')
    json.dump(prodDict, f)
    f.close()
    subprocess.call(["php","-f","../dmzToWeb.php","WomenBottomsReady.json"])

