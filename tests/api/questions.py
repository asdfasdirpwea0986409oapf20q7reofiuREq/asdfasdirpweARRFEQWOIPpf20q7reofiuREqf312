import requests
import datetime
import json

post = {"id" : 0, "authorID" : 0, "upvotes" : 10, "downvotes": 0, "answeredMemberIDs" : json.dumps([0]), "created" : str(datetime.datetime.now()), "question" : "Does this API actually work?"}

response = requests.post("https://asdfasdirpweARRFEQWOIPpf20q7reofiuREqf312.asdfasdirpwea09.repl.co/questions").text

print(response)