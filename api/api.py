from flask import *
import database
import json

app = Flask("Tackboard API")

@app.errorhandler(404)
def notFound(error):
    return jsonify({"error" : "that view function was not found", "details" : str(error)}), 404

@app.errorhandler(405)
def requestForbidden(error):
    return jsonify({"error" : "that http request is forbidden", "details" : str(error)}), 
    
@app.errorhandler(406)
def insufficientData(error):
    return jsonify({"error" : "insufficient data", "details" : str(error)}), 406

@app.route("/")
def homepage():
    if request.method == "GET":
        return jsonify({"message" : "welcome to the Tackboard api!"}), 200

@app.route("/users", methods = ["POST", "GET", "PATCH", "DELETE"])
def user():
    connection = database.users.connect()
    try:
        values = json.loads(request.get_json())
    except TypeError:
        pass # means that request is GET or faulty
    try:
        if request.method == "POST":
            database.users.create(connection, id = values["id"], created = values["created"], username = values["username"], name = values["name"], email = values["email"], asked = values["asked"], answered = values["answered"])
            return jsonify({"message" : "success"}), 201
        elif request.method == "GET":
            data = database.users.retreive(connection, int(request.args.get("id")))
            return jsonify(data), 200
        elif request.method == "PATCH":
            database.users.update(connection, values["id"], values["column"], values["new"])
            return jsonify({"message" : "success"}), 200
        elif request.method == "DELETE":
            database.users.delete(connection, values["id"])
            return jsonify({"message" : "success"}), 200
    except KeyError: # user did not pass in necessary data 
        abort(406)
    except TypeError: # user did not pass in id in url for retrieve method
        abort(406)

@app.route("/tackboards", methods = ["POST", "GET", "PATCH", "DELETE"])
def tackboard():
    connection = database.tackboards.connect()
    try:
        values = json.loads(request.get_json())
    except TypeError:
        pass # means that request is GET or faulty
    try:
        if request.method == "POST":
            database.tackboards.create(connection, id = values["id"], name = values["name"], subject = values["subject"], description = values["description"], public = values["public"], ownerID = values["ownerID"], created = values["created"], memberIDs = values["memberIDs"], questionIDs = values["questionIDs"], answersIDs = values["answersIDs"])
            return jsonify({"message" : "success"}), 201
        elif request.method == "GET":
            data = database.tackboards.retreive(connection, int(request.args.get("id")))
            return jsonify(data), 200
        elif request.method == "PATCH":
            database.tackboards.update(connection, values["id"], values["column"], values["new"])
            return jsonify({"message" : "success"}), 200
        elif request.method == "DELETE":
            database.tackboards.delete(connection, values["id"])
            return jsonify({"message" : "success"}), 200
    except KeyError: # user did not pass in necessary data 
        abort(406)
    except TypeError: # user did not pass in id in url for retrieve method
        abort(406)

@app.route("/questions", methods = ["POST", "GET", "PATCH", "DELETE"])
def question():
    connection = database.questions.connect()
    try:
        values = json.loads(request.get_json())
    except TypeError:
        pass # means that request is GET or faulty
    try:
        if request.method == "POST":
            database.questions.create(connection, id = values["id"], authorID = values["authorID"], upvotes = values["upvotes"], downvotes = values["downvotes"], answeredMemberIDs = values["answeredMemberIDs"], created = values["created"], question = values["question"])
            return jsonify({"message" : "success"}), 201
        elif request.method == "GET":
            data = database.questions.retreive(connection, int(request.args.get("id")))
            return jsonify(data), 200
        elif request.method == "PATCH":
            database.questions.update(connection, values["id"], values["column"], values["new"])
            return jsonify({"message" : "success"}), 200
        elif request.method == "DELETE":
            database.questions.delete(connection, values["id"])
            return jsonify({"message" : "success"}), 200
    except KeyError: # user did not pass in necessary data 
        abort(406)
    except TypeError: # user did not pass in id in url for retrieve method
        abort(406)

@app.route("/answers", methods = ["POST", "GET", "PATCH", "DELETE"])
def answer():
    connection = database.answers.connect()
    try:
        values = json.loads(request.get_json())
    except TypeError:
        pass # means that request is GET or faulty
    try:
        if request.method == "POST":
            database.answers.create(connection, id = values["id"], questionID = values["questionID"], authorID = values["authorID"], upvotes = values["upvotes"], downvotes = values["downvotes"], created = values["created"], answer = values["answer"])
            return jsonify({"message" : "success"}), 201
        elif request.method == "GET":
            data = database.answers.retreive(connection, int(request.args.get("id")))
            return jsonify(data), 200
        elif request.method == "PATCH":
            database.answers.update(connection, values["id"], values["column"], values["new"])
            return jsonify({"message" : "success"}), 200
        elif request.method == "DELETE":
            database.answers.delete(connection, values["id"])
            return jsonify({"message" : "success"}), 200
    except KeyError: # user did not pass in necessary data 
        abort(406)
    except TypeError: # user did not pass in id in url for retrieve method
        abort(406)

if __name__ == "__main__":
    app.run(debug = True)