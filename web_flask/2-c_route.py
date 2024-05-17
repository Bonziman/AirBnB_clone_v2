#!/usr/bin/python3
"""model that defines a simple hello world flask app"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    new_text = text.replace("_", " ")
    return f"C {new_text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
