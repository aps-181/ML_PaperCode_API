from flask import Flask, request, jsonify
from guesslang import Guess
import json
app = Flask(__name__)

port = 5000


@app.route("/")
def home():
    return "home"


@app.route('/')
def get_code_language():
    code = request.args.get("code")

    guess = Guess()
    print(code)
    name = guess.language_name(str(code))

    print(name)
    return jsonify({"language": name})


@app.route('/getLanguage', methods=["POST"])
def getLanguage():
    data = request.get_json()
    print(data['code'])
    guess = Guess()
    code = data['code']
    name = guess.language_name(str(code))

    print(name)
    return jsonify({"language": name})


port = 5000

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=port)
    app.run(debug=True)
