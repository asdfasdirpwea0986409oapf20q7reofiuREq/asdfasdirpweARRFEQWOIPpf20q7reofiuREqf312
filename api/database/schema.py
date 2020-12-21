import json

with open("C:\\Users\\rngup\\OneDrive\\Documents\\Programming\\Tackboard\\api\\database\\schema.json", "r") as file:
    content = json.load(file)

def tackboards():
    return content["tackboards"]

def users():
    return content["users"]

def questions():
    return content["questions"]

def answers():
    return content["answers"]