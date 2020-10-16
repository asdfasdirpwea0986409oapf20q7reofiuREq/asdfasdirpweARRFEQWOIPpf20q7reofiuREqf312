import requests
import datetime

res = requests.post("http://127.0.0.1:5000/delete/question/", json = {"id": 1})
if res.ok:
    print(res.text)