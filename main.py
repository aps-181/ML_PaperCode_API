from flask import Flask, request
from guesslang import Guess
app = Flask(__name__)


@app.route("/")
def home():
    return "home"


@app.route('/get-code-language')
def get_code_language():
    code = request.args.get("code")

    guess = Guess()

    name = guess.language_name(code)

    print(name)
    return name


if __name__ == "__main__":
    app.run(debug=True)
