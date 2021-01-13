import requests

url = "postman-student-expert.glitch.me/training"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
