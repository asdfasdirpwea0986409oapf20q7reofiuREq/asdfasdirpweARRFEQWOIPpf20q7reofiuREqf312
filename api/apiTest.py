import requests
import json
import datetime

postData = {"id" : 0, "authorID" : 0, "upvotes" : 1, "downvotes" : 0, "answeredMemberIDs" : json.dumps([0, 1, 2]), "created" : str(datetime.datetime.now()), "question" : "What is life?"}

patchData = {"id" : 0, "column" : "upvotes", "new" : 4}

deleteData = {"id" : 1}

res = requests.patch("http://127.0.0.1:5000/questions", json=json.dumps(patchData))

print(res.text)