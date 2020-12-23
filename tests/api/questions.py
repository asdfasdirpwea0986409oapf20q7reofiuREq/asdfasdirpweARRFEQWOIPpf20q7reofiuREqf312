import requests
import datetime
import json

post = {"id" : 1, "authorID" : 0, "upvotes" : 10, "downvotes": 0, "answeredMemberIDs" : json.dumps([0]), "created" : str(datetime.datetime.now()), "question" : "Who am I?"}

patch = {"id" : 1, "column" : "upvotes", "new" : 999}

delete = {"id" : 1}

response = requests.delete("https://asdfasdirpwearrfeqwoippf20q7reofiureqf312.asdfasdirpwea09.repl.co/questions", json = json.dumps(delete))

print(response.text)