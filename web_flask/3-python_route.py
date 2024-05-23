#!/usr/bin/env python3
"""
Script that start a Flask web application.
"""


from flask import Flask


app = Flask(__name__)



@app.route('/', strict_slashes=False)
def home():
    """
    Display 'Hello HBNB!'.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display 'HBNB'.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display 'C ' followed by the value of <text>.
    """
    text_no_underscore = text.replace('_', ' ')
    return 'C {}'.format(text_no_underscore)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """
    Display 'Python ' followed by text from html request with default
    text 'is cool'.
    """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
