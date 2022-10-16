import requests

url = 'http://127.0.0.1:8000/api/spend/'

response = requests.post(url, json={'points':5000})
print(response)
print(response.json())


