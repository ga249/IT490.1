import requests
import jsonParser
import time
import json
import subprocess

headers = {"X-RapidAPI-Key": "9b85d9f314msh3853180041bdc74p1def30jsnb8c7527a68fb", "X-RapidAPI-Host": "unofficial-shein.p.rapidapi.com"}

def grabMenShirts():
    querystring = {"keywords":"Mens Shirts","language":"en","country":"US","currency":"USD","sort":"7","limit":"20","page":"1"}
    url = "https://unofficial-shein.p.rapidapi.com/products/search"
    response = requests.request("GET", url, headers=headers, params=querystring)
    if len(response.text) == 0:
        subprocess.call(["php","-f","../publishLog.php","API request failed for Mens Shirts"])
        print("API request failed for Mens Shirts")
        return False
    f = open("MenShirtApiData.json", 'w')
    f.write(response.text)
    f.close()
    return True

def grabMensPants():
    querystring = {"keywords":"Mens Pants","language":"en","country":"US","currency":"USD","sort":"7","limit":"20","page":"1"}
    url = "https://unofficial-shein.p.rapidapi.com/products/search"
    response = requests.request("GET", url, headers=headers, params=querystring)
    if len(response.text) == 0:
        subprocess.call(["php","-f","../publishLog.php","API request failed for Mens Pants"])
        print("API request failed for Mens Pants")
        return False
    f = open("MenPantsApiData.json", 'w')
    f.write(response.text)
    f.close()
    return True

def grabWomenTops():
    querystring = {"keywords":"Womens Tops","language":"en","country":"US","currency":"USD","sort":"7","limit":"20","page":"1"}
    url = "https://unofficial-shein.p.rapidapi.com/products/search"
    response = requests.request("GET", url, headers=headers, params=querystring)
    if len(response.text) == 0:
        subprocess.call(["php","-f","../publishLog.php","API request failed for Womens Shirts"])
        print("API request failed for Womens Shirts")
        return False
    f = open("WomenTopsApiData.json", 'w')
    f.write(response.text)
    f.close()
    return True

def grabWomenBottoms():
    querystring = {"keywords":"Womens Bottoms","language":"en","country":"US","currency":"USD","sort":"7","limit":"20","page":"1"}
    url = "https://unofficial-shein.p.rapidapi.com/products/search"
    response = requests.request("GET", url, headers=headers, params=querystring)
    if len(response.text) == 0:
        subprocess.call(["php","-f","../publishLog.php","API request failed for Womens Shirts"])
        print("API request failed for Womens Shirts")
        return False
    f = open("WomenBottomApiData.json", 'w')
    f.write(response.text)
    f.close()
    return True
    
def grabDetails(goodsIdList, gender):
    url = "https://unofficial-shein.p.rapidapi.com/products/detail"
    prodDict = {}
    index = 1
    for ID in goodsIdList:
        if index % 4 == 0:
            time.sleep(1)
        querystring = {"goods_id":ID,"language":"en","country":"US","currency":"USD"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        if len(response.text) == 0:
            print("API product details request failed for prodID: " + ID)
            print(response.text)
            return False
        f = open("temp.json", 'w')
        f.write(response.text)
        f.close()
        f = open("temp.json")
        data = json.load(f)
        f.close()
        prodDict['prod'+str(index)] = jsonParser.parseDetails(data, gender)
        index += 1
    return prodDict   






    
