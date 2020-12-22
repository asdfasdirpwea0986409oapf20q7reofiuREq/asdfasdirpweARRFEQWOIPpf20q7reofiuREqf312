import requests
import datetime
import json

post = {"id" : 0, "authorID" : 0, "upvotes" : 10, "downvotes": 0, "answeredMemberIDs" : json.dumps([0]), "created" : str(datetime.datetime.now()), "question" : "Does this API actually work?"}

response = requests.post("http://127.0.0.1:5000/questions", json = json.dumps(post))

print(response.text)