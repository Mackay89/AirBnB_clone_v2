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
def c_is_fun(text):
    """
    Display 'C ' followed by the value of <text>.
    """
    text_no_underscore = text.replace('_', ' ')
    return 'C {}'.format(text_no_underscore)


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_with_text(text):
    """
    Display 'Python ' followed by the value text.
    """
    text_no_underscore = text.replace('_', ' ')
    return "Python {}" .format(text_no_underscore)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
