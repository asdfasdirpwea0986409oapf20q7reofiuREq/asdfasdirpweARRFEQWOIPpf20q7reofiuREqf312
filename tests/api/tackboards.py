import requests
import datetime
import json

post = {"id" : 0, "name" : "test", "subject" : "testing", "description" : "testing", "public" : 0, "ownerID" : 0, "created" : str(datetime.datetime.now()), "memberIDs" : json.dumps([]), "questionIDs" : json.dumps([0]), "answersIDs" : json.dumps([0])}

patch = {"id" : 0, "column" : "public", "new" : 0}

delete = {"id" : 0}

response = requests.post("http://127.0.0.1:5000/tackboards", json = json.dumps(post))

print(response.text)