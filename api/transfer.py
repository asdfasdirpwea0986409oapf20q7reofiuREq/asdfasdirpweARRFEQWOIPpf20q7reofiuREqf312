import argparse
import sqlite3
import database
import pprint
import json
import os

class Schema:
    def __init__(self, connection):
        self.connection = connection
        self.users()
        self.tackboards()
        self.questions()
        self.answers()

    def users(self):
        try:
            self.connection.execute("""CREATE TABLE users (
    id integer UNIQUE,
    created text,
    username text,
    name text,
    email text, 
    asked integer,
    answered integer
);""")
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def tackboards(self):
        try:
            self.connection.execute("""CREATE TABLE tackboards (
    id integer UNIQUE,
    name text,
    subject text,
    description text,
    public integer,
    ownerID integer,
    created text,
    memberIDs text,
    questionIDs text,
    answersIDs text
);""")
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def questions(self):
        try:
            self.connection.execute("""CREATE TABLE questions (
    id integer UNIQUE,
    authorID integer,
    upvotes integer,
    downvotes integer,
    answeredMemberIDs text,
    created text,
    question text
);""")
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def answers(self):
        try:
            self.connection.execute("""CREATE TABLE answers (
    id integer UNIQUE,
    questionID integer,
    authorID integer,
    upvotes integer,
    downvotes integer,
    created text,
    answer text
);""")
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

class Retrieve:
    def __init__(self):
        self.url = "C:\\Users\\rngup\\OneDrive\\Documents\\Programming\\Tackboard\\api\\database\\database.db"

    def connect(self): 
        return sqlite3.connect(self.url)

    def users(self, connection):
        cursor = connection.execute("SELECT * from users")
        output = []
        for row in cursor:
            entry = {}
            entry["id"] = row[0]
            entry["created"] = row[1]
            entry["username"] = row[2]
            entry["name"] = row[3]
            entry["email"] = row[4]
            entry["asked"] = row[5]
            entry["answered"] = row[6]
            output.append(entry)
        return output

    def tackboards(self, connection):
        cursor = connection.execute("SELECT * from tackboards")
        output = []
        for row in cursor:
            entry = {}
            entry["id"] = row[0]
            entry["name"] = row[1]
            entry["subject"] = row[2]
            entry["description"] = row[3]
            entry["public"] = row[4]
            entry["ownerID"] = row[5]
            entry["created"] = row[6]
            entry["memberIDs"] = row[7]
            entry["questionIDs"] = row[8]
            entry["answersIDs"] = row[9]
            output.append(entry)
        return output

    def questions(self, connection):
        cursor = connection.execute("SELECT * from questions")
        output = []
        for row in cursor:
            entry = {}
            entry["id"] = row[0]
            entry["authorID"] = row[1]
            entry["upvotes"] = row[2]
            entry["downvotes"] = row[3]
            entry["answeredMemberIDs"] = row[4]
            entry["created"] = row[5]
            entry["question"] = row[6]
            output.append(entry)
        return output

    def answers(self, connection):
        cursor = connection.execute("SELECT * from answers")
        output = []
        for row in cursor:
            entry = {}
            entry["id"] = row[0]
            entry["questionID"] = row[1]
            entry["authorID"] = row[2]
            entry["upvotes"] = row[3]
            entry["downvotes"] = row[4]
            entry["created"] = row[5]
            entry["answer"] = row[6]
            output.append(entry)
        return output

class Create:
    def __init__(self):
        self.url = "C:\\Users\\rngup\\OneDrive\\Documents\\Programming\\Tackboard\\api\\database\\database.db"

    def connect(self): 
        return sqlite3.connect(self.url)
    
    def users(self, connection, all):
        for data in all:
            while True:
                try:
                    data = (data["id"], data["created"], data["username"], data["name"], data["email"], data["asked"], data["answered"])
                    connection.execute(f"INSERT INTO users ('id', 'created', 'username', 'name', 'email', 'asked', 'answered') VALUES {data}")
                    connection.commit()
                    break
                except sqlite3.IntegrityError:
                    data["id"] +=1
                    continue


    def tackboards(self, connection, all):
        for data in all:
            while True:
                try:
                    formatedData = (data["id"], data["name"], data["subject"], data["description"], data["public"], data["ownerID"], data["created"], data["memberIDs"], data["questionIDs"], data["answersIDs"])
                    connection.execute(f"INSERT INTO tackboards ('id', 'name', 'subject', 'description', 'public', 'ownerID', 'created', 'memberIDs', 'questionIDs', 'answersIDs') VALUES {formatedData}")
                    connection.commit()
                    break
                except sqlite3.IntegrityError:
                    data["id"] +=1
                    continue
    
    def questions(self, connection, all):
        for data in all:
            while True:
                try:
                    formatedData = (data["id"], data["authorID"], data["upvotes"], data["downvotes"], data["answeredMemberIDs"], data["created"], data["question"])
                    connection.execute(f"INSERT INTO questions ('id', 'authorID', 'upvotes', 'downvotes', 'answeredMemberIDs', 'created', 'question') VALUES {formatedData}")
                    connection.commit()
                    break
                except sqlite3.IntegrityError:
                    data["id"] +=1
                    continue
    
    def answers(self, connection, all):
        for data in all:
            while True:
                try:
                    formatedData = (data["id"], data["questionID"], data["authorID"], data["upvotes"], data["downvotes"], data["created"], data["answer"])
                    connection.execute(f"INSERT INTO answers ('id', 'questionID', 'authorID', 'upvotes', 'downvotes', 'created', 'answer') VALUES {formatedData}")
                    connection.commit()
                    break
                except sqlite3.IntegrityError:
                    data["id"] +=1
                    continue

def importData():
    create = Create()
    connection = create.connect()
    Schema(connection)
    filepath = input("Path of the file with exported data: ")
    with open(filepath, "r") as file:
        data = json.load(file)
    print("[INFO] Import started")
    create.users(connection, data["users"])
    create.tackboards(connection, data["tackboards"])
    create.questions(connection, data["questions"])
    create.answers(connection, data["answers"])
    print("[INFO] Import complete")
    print("[INFO] Database has all data")

def export():
    retrieve = Retrieve()
    connection = retrieve.connect()
    printer = pprint.PrettyPrinter(indent = 4)
    print("[INFO] Export started")
    data = {
        "users" : retrieve.users(connection),
        "tackboards" : retrieve.tackboards(connection),
        "questions" : retrieve.questions(connection),
        "answers" : retrieve.answers(connection)
    }
    print("[INFO] Exported data: -------------------------------------------------------------------------------")
    printer.pprint(data)
    print("-----------------------------------------------------------------------------------------------------")
    return data

parser = argparse.ArgumentParser()
parser.add_argument("action", help = "import/export")
args = parser.parse_args()
action = args.action
if action == "import":
    importData()
elif action == "export":
    exported = export()
    with open("exported.json", "w") as file:
        file.truncate(0)
        file.write(json.dumps(exported))
    print("[INFO] Exported Data Put Into File: 'exported.json'")
