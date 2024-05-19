#!/usr/bin/env python3
"""
Script that start a Flask web application.
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Return 'Hello HBNB!' on the root route.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Return 'HBNB' on the /hbnb route.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_route(text):
    """
    Return 'C ' followed by the value of text variable.
    Replace underscore _ symbols with a space.
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', defaults={'text': 'is cool'})
def python_text(text):
    """
    Return 'Python ' followed by the value of the text.
    Replace underscore _ symbols with a space. Default value of text is "is cool".
    """
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
