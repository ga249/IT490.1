import requests

url = "https://unofficial-shein.p.rapidapi.com/products/search"

querystring = {"keywords":"Mens Shirts","language":"en","country":"US","currency":"USD","sort":"7","limit":"20","page":"1"}

headers = {
	"X-RapidAPI-Key": "9b85d9f314msh3853180041bdc74p1def30jsnb8c7527a68fb",
	"X-RapidAPI-Host": "unofficial-shein.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

