import requests

response = requests.get('http://ip-api.com/json/')
geodata = response.json()

print('Country:', geodata['country'])
print('Region:', geodata['regionName'])
