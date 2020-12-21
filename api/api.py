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
    except KeyError:
        abort(406)

if __name__ == "__main__":
    app.run(debug = True)