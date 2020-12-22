import sqlite3
import database.schema
import os

columns = tuple(database.schema.users())

def connect():
    connection = sqlite3.connect(os.getcwd() + "\\api\\database\\database.db", check_same_thread = False) # check_same_thread allows us to run threaded queries
    try:
        connection.execute("""CREATE TABLE users (
    id integer UNIQUE,
    created text,
    username text,
    name text,
    email text, 
    asked integer,
    answered integer
);""")
        connection.commit()
    except sqlite3.OperationalError:
        pass
    return connection

def create(connection, **values):
    while True:
        try:
            data = (values["id"], values["created"], values["username"], values["name"], values["email"], values["asked"], values["answered"])
            connection.execute(f"INSERT INTO users {columns} VALUES {data}")
            connection.commit()
            break
        except sqlite3.IntegrityError:
            values["id"] +=1
            continue

def retreive(connection, id):
    cursor = connection.execute(f"SELECT * from users")
    for row in cursor:
        if row[0] == id:
            output = {}
            output["id"] = row[0]
            output["created"] = row[1]
            output["username"] = row[2]
            output["name"] = row[3]
            output["email"] = row[4]
            output["asked"] = row[5]
            output["answered"] = row[6]
            return output
        else:
            pass
    return {"error": "id does not corrolate with any data"}

def update(connection, id, column, new):
    connection.execute(f"UPDATE users SET {column} = '{new}' WHERE id = {id}")
    connection.commit()

def delete(connection, id):
    connection.execute(f"DELETE FROM users WHERE id = {id}")
    connection.commit()