#!/usr/bin/env python3
"""
Script that start a Flask web application.
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Return Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Return HBNB.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """
    Display 'C ' followed by the value of text variable.
    Replace underscore _ symbols with a space.
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', defaults={'text': 'is cool'})
def python_route(text):
    """
    Display 'Python ' followed by the value of the text.
    Replace underscore _ symbols with a space. Default value of text is "is cool".
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
