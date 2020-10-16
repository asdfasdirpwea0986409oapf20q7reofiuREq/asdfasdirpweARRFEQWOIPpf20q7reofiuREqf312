import sqlite3
import json
import datetime

connection = sqlite3.connect("C:\\Users\\rngup\\OneDrive\\Documents\\Programming\\Tackboard\\database\database.db")
columnNames = ["questionID", "question", "authorID", "created"]

def connect():
    try:
        connection.execute("""CREATE TABLE question (
    questionID integer PRIMARY KEY AUTOINCREMENT,
    question text,
    authorID integer,
    created string
);""")
        connection.commit()
    except sqlite3.OperationalError:
        pass

def create(values):
    while True:
        try:
            connection.execute(f"INSERT INTO question {tuple(columnNames)} VALUES {tuple(values)};")
            connection.commit()
            break
        except sqlite3.IntegrityError:
            values[0] +=1
            continue

def retreive(id):
    cursor = connection.execute(f"SELECT * from question WHERE {columnNames[0]} = {id}")
    for row in cursor:
        if row[0] == id:
            output = {}
            output["questionID"] = row[0]
            output["question"] = row[1]
            output["authorID"] = row[2]
            output["created"] = row[3]
            return json.dumps(output, indent = 4)
        else:
            pass
    return json.dumps({"Error": "Question ID does not corrolate with any data"}, indent = 4)

def update(id, column, newValue):
    connection.execute(f"UPDATE question SET {column} = '{newValue}' WHERE {columnNames[0]} = {id}")
    connection.commit()

def delete(id):
    connection.execute(f"DELETE FROM question WHERE {columnNames[0]} = {id}")
    connection.commit()

def unitTest():
    connect()
    # create([1, "Placeholder?", 1, str(datetime.datetime.now())])
    print(retreive(1))
    # update(1, "question", "Placeholder?!")
    # print(retreive(1))
    # print(retreive(10))
    # delete(1)
    # print(retreive(1))
    connection.close()