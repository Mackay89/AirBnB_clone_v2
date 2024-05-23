#!/usr/bin/python3
"""
Script that stats a Flask web application
"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """
    Return 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    Return 'HBNB'
    """
    return 'HBNB'

@app.route('/c/<text>')
def c_route1(text):
    """
    Display 'C ' followed by the text from html request
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """
    Return 'Python ' followed by text from html request with default
    text 'is cool'
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/numbert_template/<int:n>')
def number_template(n):
    """
    Return html template containing the number 'n'
    """
    return render_template('number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """
    Return an html page starting whether the number n is even or odd.
    """
    if n % 2 == 0:
        return render_template('odd_or_even.html', number=n, result='even')
    else:
        return render_template('even_odd.html', number=n, result='odd')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
