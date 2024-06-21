import requests

url = 'http://0.0.0.0:8080/upload'
file = {'file': open('/t1.jpg', 'rb')}
resp = requests.post(url=url, files=file)
print(resp.json())


url = 'http://0.0.0.0:8080/predict'
resp = requests.get(url=url)
print(resp.json())