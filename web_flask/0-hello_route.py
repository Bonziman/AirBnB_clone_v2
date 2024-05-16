#!/usr/bin/python3
"""model that defines a simple hello world flask app"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello HBNB!"
