from flask import Flask, request
from flask_cors import CORS
from algo import Algo
from repo.db.database import create_user_in_db
app = Flask(__name__)
CORS(app)

@app.route("/mem")
def default():
    return {"message": ['one', 'two', 'three']}

@app.route("/algo")
def funone():
    bot = Algo(66369401, "vkkwwa1h", "MetaQuotes-Demo")
    bot.run()
    return {"message": ['one', 'two', 'three']}

@app.route(f"/create", methods=['POST'])
def create_new_user():
    args = request.get_json()
    name = args.get("name")
    email = args.get("email")
    password = args.get("password")
    print(name)
    db_resp = create_user_in_db(email, name, password)
    return {'name': name, 'email': email, "res": db_resp}

if __name__ == "__main__":
    app.run(debug=True)

