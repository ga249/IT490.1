import json
import subprocess

#def parseJson(file):
#    productDict = {}
#    f = open(file)
#    data = json.load(f)
#    index = 1
#    for product in data['info']['products']:
#        productDict['prod'+str(index)] = {'goods_id': product['goods_id'], 'goods_name': product['goods_name'], 'goods_img': product['goods_img']}
#        index += 1
#    print(productDict)

def getPIDfromJson(file):
    pidList = []
    f = open(file)
    data = json.load(f)
    for product in data['info']['products']:
        pidList.append(product['goods_id'])
    if len(pidList) != 20:
        subprocess.call(["php","-f","../publishLog.php","error parser:21 didn't get all pid's"])
        print("error parser: didn't get all pid's")
        print(str(len(pidList)) + " ID's grabbed")
    f.close()
    return pidList
    
#Returns dict of goodsID, goodsName, originalImg, gender, color
def parseDetails(data, gender):
    detailedProdDict = {}
    detailedProdDict['PID'] = data['info']['goods_id']
    detailedProdDict['name'] = data['info']['goods_name']
    detailedProdDict['img'] = data['info']['original_img']
    detailedProdDict['gender'] = gender
    detailedProdDict['color'] = data['info']['productDetails'][0]['attr_value']
    return detailedProdDict
    

        

#parseJson('MenShirtApiData.json')


