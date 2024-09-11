import requests


response = requests.get('http://127.0.0.1:8002/change')
print(response.status_code)
print(response.text)
