import sqlite3
import database.schema
import os

columns = tuple(database.schema.tackboards())

def connect():
    connection = sqlite3.connect(os.getcwd() + "\\api\\database\\database.db", check_same_thread = False) # check_same_thread allows us to run threaded queries
    try:
        connection.execute("""CREATE TABLE tackboards (
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
        connection.commit()
    except sqlite3.OperationalError:
        pass
    return connection

def create(connection, **values):
    while True:
        try:
            data = (values["id"], values["name"], values["subject"], values["description"], values["public"], values["ownerID"], values["created"], values["memberIDs"], values["questionIDs"], values["answersIDs"])
            connection.execute(f"INSERT INTO tackboards {columns} VALUES {data}")
            connection.commit()
            break
        except sqlite3.IntegrityError:
            values["id"] +=1
            continue

def retreive(connection, id):
    cursor = connection.execute(f"SELECT * from tackboards")
    for row in cursor:
        if row[0] == id:
            output = {}
            output["id"] = row[0]
            output["name"] = row[1]
            output["subject"] = row[2]
            output["description"] = row[3]
            output["public"] = row[4]
            output["ownerID"] = row[5]
            output["created"] = row[6]
            output["memberIDs"] = row[7]
            output["questionIDs"] = row[8]
            output["answersIDs"] = row[9]
            return output
        else:
            pass
    return {"error": "id does not corrolate with any data"}

def update(connection, id, column, new):
    connection.execute(f"UPDATE tackboards SET {column} = '{new}' WHERE id = {id}")
    connection.commit()

def delete(connection, id):
    connection.execute(f"DELETE FROM tackboards WHERE id = {id}")
    connection.commit()