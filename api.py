from flask import *
import database

app = Flask(__name__)

"""
TODO: Remove 'GET' requests
TODO: Create endpoints for question, answer, and user; allow methods used to run the needed code
"""

@app.route("/", methods = ["GET"])
def homepage():
    return jsonify({"Response": "Welcome to Zeus!"})

@app.route("/create/question/", methods = ["GET", "POST"])
def createQuestion():
    if request.method == "GET":
        return jsonify({"Error": "llegal Request"})
    else:
        postJSON = request.get_json(force = True)
        database.question.create(list(postJSON["values"]))
        return jsonify({"Response": "Success"})

@app.route("/create/answer/", methods = ["GET", "POST"])
def createAnswer():
    if request.method == "GET":
        return jsonify({"Error": "llegal Request"})
    else:
        postJSON = request.get_json(force = True)
        database.answer.create(list(postJSON["values"]))
        return jsonify({"Response": "Success"})

@app.route("/create/user/", methods = ["GET", "POST"])
def createUser():
    if request.method == "GET":
        return jsonify({"Error": "llegal Request"})
    else:
        postJSON = request.get_json(force = True)
        database.user.create(list(postJSON["values"]))
        return jsonify({"Response": "Success"})

@app.route("/retrieve/question/questionID/<id>")
def retrieveQuestion(id):
    return database.question.retreive(int(id))

@app.route("/retrieve/answer/answerID/<id>")
def retrieveAnswer(id):
    return database.answer.retreive(int(id))

@app.route("/retrieve/answer/questionID/<id>")
def retreiveAnswerbyQuestion(id):
    return database.answer.retreiveAnswerbyQuestion(int(id))

@app.route("/retrieve/user/userID/<id>")
def retreiveUser(id):
    return database.user.retreive(int(id))

@app.route("/update/question/", methods = ["GET", "POST"])
def updateQuestion():
    if request.method == "GET":
        return jsonify({"Error": "llegal Request"})
    else:
        postJSON = request.get_json(force = True)
        id = postJSON["id"]
        column = postJSON["column"]
        newValue = postJSON["newValue"]
        database.question.update(id, column, newValue)
        return jsonify({"Response": "Success"})

@app.route("/update/answer/", methods = ["GET", "POST"])
def updateAnswer():
    if request.method == "GET":
        return jsonify({"Error": "llegal Request"})
    else:
        postJSON = request.get_json(force = True)
        id = postJSON["id"]
        column = postJSON["column"]
        newValue = postJSON["newValue"]
        database.answer.update(id, column, newValue)
        return jsonify({"Response": "Success"})

@app.route("/update/user/", methods = ["GET", "POST"])
def updateUser():
    if request.method == "GET":
        return jsonify({"Error": "llegal Request"})
    else:
        postJSON = request.get_json(force = True)
        id = postJSON["id"]
        column = postJSON["column"]
        newValue = postJSON["newValue"]
        database.user.update(id, column, newValue)
        return jsonify({"Response": "Success"})

@app.route("/delete/question/", methods = ["GET", "POST"])
def deleteQuestion():
    if request.method == "GET":
        return jsonify({"Error": "Illegal Request"})
    else:
        postJSON = request.get_json(force = True)
        id = postJSON["id"]
        database.question.delete(id)
        return jsonify({"Response": "Success"})

@app.route("/delete/answer/", methods = ["GET", "POST"])
def deleteAnswer():
    if request.method == "GET":
        return jsonify({"Error": "Illegal Request"})
    else:
        postJSON = request.get_json(force = True)
        id = postJSON["id"]
        database.answer.delete(id)
        return jsonify({"Response": "Success"})

@app.route("/delete/user/", methods = ["GET", "POST"])
def deleteUser():
    if request.method == "GET":
        return jsonify({"Error": "Illegal Request"})
    else:
        postJSON = request.get_json(force = True)
        id = postJSON["id"]
        database.user.delete(id)
        return jsonify({"Response": "Success"})

if __name__ == "__main__":
    app.run(debug = True)