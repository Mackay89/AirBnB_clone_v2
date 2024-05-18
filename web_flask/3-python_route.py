#!/usr/bin/env python3
"""
Script that start a Flask web application.
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display 'Hello HBNB!' on the root route.
    """
    return "hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' on the /hbnb route."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=Flask)
def c_text(text):
    """
    Display 'C ' followed by thevalue of text.

    Args:
        text (str); The text to display, with underscores replaced by spaces.


    Reterns:
        str: The formatted string to be displayed.
    """
    return "Python " +text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Display 'Python ' followed by the value of the text.

    If no text is provided, the default value 'is cool' is used.

    Args:
        text (str): The text to display, with underscores replaced by spaces.

    Returns:
        str: The formatted string to be displayed.
    """
    return "Python " + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

