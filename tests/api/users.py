import requests
import datetime
import json

post = {"id" : 0, "created" : str(datetime.datetime.now()), "username" : "hello", "name" : "hello", "email" : "hi@hello.greet", "asked" : 0, "answered": 20}

patch = {"id" : 0, "column" : "answered", "new" : 21}

delete = {"id" : 0}

response = requests.post("http://127.0.0.1:5000/users", json = json.dumps(post))

print(response.text)