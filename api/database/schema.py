import json
import os

with open(os.getcwd() + "\\api\\database\\schema.json", "r") as file:
    content = json.load(file)

def tackboards():
    return content["tackboards"]

def users():
    return content["users"]

def questions():
    return content["questions"]

def answers():
    return content["answers"]