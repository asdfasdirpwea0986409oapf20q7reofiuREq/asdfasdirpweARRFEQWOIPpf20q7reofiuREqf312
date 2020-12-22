import sqlite3
import database.schema
import os

columns = tuple(database.schema.questions())

def connect():
    connection = sqlite3.connect(os.getcwd() + "\\api\\database\\database.db", check_same_thread = False) # check_same_thread allows us to run threaded queries
    try:
        connection.execute("""CREATE TABLE questions (
    id integer UNIQUE,
    authorID integer,
    upvotes integer,
    downvotes integer,
    answeredMemberIDs text,
    created text,
    question text
);""")
        connection.commit()
    except sqlite3.OperationalError:
        pass
    return connection

def create(connection, **values):
    while True:
        try:
            data = (values["id"], values["authorID"], values["upvotes"], values["downvotes"], values["answeredMemberIDs"], values["created"], values["question"])
            connection.execute(f"INSERT INTO questions {columns} VALUES {data}")
            connection.commit()
            break
        except sqlite3.IntegrityError:
            values["id"] +=1
            continue

def retreive(connection, id):
    cursor = connection.execute(f"SELECT * from questions")
    for row in cursor:
        if row[0] == id:
            output = {}
            output["id"] = row[0]
            output["authorID"] = row[1]
            output["upvotes"] = row[2]
            output["downvotes"] = row[3]
            output["answeredMemberIDs"] = row[4]
            output["created"] = row[5]
            output["question"] = row[6]
            return output
        else:
            pass
    return {"error": "id does not corrolate with any data"}

def update(connection, id, column, new):
    connection.execute(f"UPDATE questions SET {column} = '{new}' WHERE id = {id}")
    connection.commit()

def delete(connection, id):
    connection.execute(f"DELETE FROM questions WHERE id = {id}")
    connection.commit()