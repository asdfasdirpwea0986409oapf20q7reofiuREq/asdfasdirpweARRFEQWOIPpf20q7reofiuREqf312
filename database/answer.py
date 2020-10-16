import sqlite3
import json
import datetime

columnNames = ["answerID", "questionID", "answer", "authorID", "created"]
connection = sqlite3.connect("C:\\Users\\rngup\\OneDrive\\Documents\\Programming\\Tackboard\\database\database.db", check_same_thread = False)

def connect():
    try:
        connection.execute("""CREATE TABLE answer (
    answerID integer PRIMARY KEY AUTOINCREMENT,
    questionID integer,
    answer text,
    authorID integer,
    created string
);""")
        connection.commit()
    except sqlite3.OperationalError:
        pass

def create(values):
    while True:
        try:
            connection.execute(f"INSERT INTO answer {tuple(columnNames)} VALUES {tuple(values)};")
            connection.commit()
            break
        except sqlite3.IntegrityError:
            values[0] +=1
            continue

def retreive(id):
    cursor = connection.execute(f"SELECT * from answer WHERE {columnNames[0]} = {id}")
    for row in cursor:
        output = {}
        output["answerID"] = row[0]
        output["questionID"] = row[1]
        output["answer"] = row[2]
        output["authorID"] = row[3]
        output["created"] = row[4]
        return json.dumps(output, indent = 4)
    return json.dumps({"Error": "Answer ID does not corrolate with any data"}, indent = 4)

def retreiveAnswerbyQuestion(questionID):
    cursor = connection.execute(f"SELECT * from answer WHERE {columnNames[1]} = {questionID}")
    output = []
    for row in cursor:
        innerOutput = {}
        innerOutput["answerID"] = row[0]
        innerOutput["questionID"] = row[1]
        innerOutput["answer"] = row[2]
        innerOutput["authorID"] = row[3]
        innerOutput["created"] = row[4]
        output.append(innerOutput)
    if json.dumps(output, indent = 4) == "[]":
        return json.dumps({"Error": "Question ID does not corrolate with any data"}, indent = 4)
    else:
        return json.dumps(output, indent = 4)

def update(id, column, newValue):
    connection.execute(f"UPDATE answer SET {column} = '{newValue}' WHERE {columnNames[0]} = {id}")
    connection.commit()

def delete(id):
    connection.execute(f"DELETE FROM answer WHERE {columnNames[0]} = {id}")
    connection.commit()

def unitTest():
    connect()
    # create([2, 1, "Placeholders", "1", str(datetime.datetime.now())])
    # create([1, 1, "Placeholders", "1", str(datetime.datetime.now())])
    print(retreiveAnswerbyQuestion(1))
    # update(1, "answer", "Placeholder!")
    # print(retreive(1))
    # print(retreive(10))
    # delete(1)
    # print(retreive(1))
    connection.close()