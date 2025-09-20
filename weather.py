import requests
import json

url = "https://open-weather13.p.rapidapi.com/city"

querystring = {"city":"pune","lang":"EN"}

'''headers = {
	"x-rapidapi-key": "0d6f090d31msh7c271f2078d1839p1872f4jsncf12481e6b69",
	"x-rapidapi-host": "open-weather13.p.rapidapi.com"
}'''

response = requests.get(url, headers=headers, params=querystring)

#print(response.json())
print(json.dumps(response.json(),indent=4))
