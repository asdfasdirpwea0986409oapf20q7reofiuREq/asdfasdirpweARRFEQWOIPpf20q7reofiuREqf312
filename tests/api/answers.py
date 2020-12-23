import requests
import datetime
import json

post = {"id" : 0, "questionID" : 0, "authorID" : 0, "upvotes" : 10, "downvotes" : 0, "created" : str(datetime.datetime.now()), "answer" : "testing"}

patch = {"id" : 0, "column" : "answer", "new" : "testing?"}

delete = {"id" : 0}

response = requests.post("http://127.0.0.1:5000/answers", json = json.dumps(post))

print(response.text)