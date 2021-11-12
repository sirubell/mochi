import requsets

Base = "http://127.0.0.1:5000"

response = requests.get(BASE + "problem")
print(response.json())

