import sqlite3
import database.schema
import os

columns = tuple(database.schema.answers())

def connect():
    connection = sqlite3.connect(os.getcwd() + "\\api\\database\\database.db", check_same_thread = False) # check_same_thread allows us to run threaded queries
    try:
        connection.execute("""CREATE TABLE answers (
    id integer UNIQUE,
    questionID integer,
    authorID integer,
    upvotes integer,
    downvotes integer,
    created text,
    answer text
);""")
        connection.commit()
    except sqlite3.OperationalError:
        pass
    return connection

def create(connection, **values):
    while True:
        try:
            data = (values["id"], values["questionID"], values["authorID"], values["upvotes"], values["downvotes"], values["created"], values["answer"])
            connection.execute(f"INSERT INTO answers {columns} VALUES {data}")
            connection.commit()
            break
        except sqlite3.IntegrityError:
            values["id"] +=1
            continue

def retreive(connection, id):
    cursor = connection.execute(f"SELECT * from answers")
    for row in cursor:
        if row[0] == id:
            output = {}
            output["id"] = row[0]
            output["questionID"] = row[1]
            output["authorID"] = row[2]
            output["upvotes"] = row[3]
            output["downvotes"] = row[4]
            output["created"] = row[5]
            output["answer"] = row[6]
            return output
        else:
            pass
    return {"error": "id does not corrolate with any data"}

def update(connection, id, column, new):
    connection.execute(f"UPDATE answers SET {column} = '{new}' WHERE id = {id}")
    connection.commit()

def delete(connection, id):
    connection.execute(f"DELETE FROM answers WHERE id = {id}")
    connection.commit()