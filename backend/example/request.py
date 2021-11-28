import requests

BASE = "http://127.0.0.1:5000"

response = requests.post(BASE + "/problem",{"questioner_id":87,"name":"test","difficulty":2,"content":"123","time_limit":1,"memory_limit":1024,"is_hidden":0})
print(response.json())