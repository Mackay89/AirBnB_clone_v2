#!/usr/bin/python3
"""
Script that start a flask web apllication
"""


from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
    """
    Return text
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
