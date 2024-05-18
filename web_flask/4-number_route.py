#!/usr/bin/python3
"""
Scriptthat starts a Flask web application.
"""


from flask import Flask


app = Flask(__name__)


app.route('/', strict_slashes=False)
def hello():
    """
    Display 'Hello HBNB!'
    """
    return  "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display 'HBNB'.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route to display 'C ', followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Route to display 'Python ', followed by the value of the text variable.
    Replace underscore  _ symbols with a space. Default value of text is  "is cool".
    """
    return "Python {}".formate(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route to display 'n is a number' only if n is an integer.
    """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
