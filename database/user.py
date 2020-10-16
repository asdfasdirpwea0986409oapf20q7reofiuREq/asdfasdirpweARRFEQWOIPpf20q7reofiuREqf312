import sqlite3
import json
import datetime

columnNames = ["userID", "username", "password"]
connection = sqlite3.connect("C:\\Users\\rngup\\OneDrive\\Documents\\Programming\\Tackboard\\database\database.db")

def connect():
    try:
        connection.execute("""CREATE TABLE user (
    userID integer PRIMARY KEY AUTOINCREMENT,
    username text,
    password string
);""")
        connection.commit()
    except sqlite3.OperationalError:
        pass

def create(values):
    while True:
        try:
            connection.execute(f"INSERT INTO user {tuple(columnNames)} VALUES {tuple(values)};")
            connection.commit()
            break
        except sqlite3.IntegrityError:
            values[0] +=1
            continue

def retreive(id):
    cursor = connection.execute(f"SELECT * from user WHERE {columnNames[0]} = {id}")
    for row in cursor:
        if row[0] == id:
            output = {}
            output["userID"] = row[0]
            output["username"] = row[1]
            output["password"] = row[2]
            return json.dumps(output, indent = 4)
        else:
            pass
    return json.dumps({"Error": "User ID does not corrolate with any data"}, indent = 4)

def update(id, column, newValue):
    connection.execute(f"UPDATE user SET {column} = '{newValue}' WHERE {columnNames[0]} = {id}")
    connection.commit()

def delete(id):
    connection.execute(f"DELETE FROM user WHERE {columnNames[0]} = {id}")
    connection.commit()

def unitTest():
    connect()
    # create([1, "aarushgupta", "testPass"])
    print(retreive(1))
    # update(1, "username", "aargup")
    # print(retreive(1))
    # print(retreive(10))
    # delete(2)
    # print(retreive(1))
    connection.close()

unitTest()