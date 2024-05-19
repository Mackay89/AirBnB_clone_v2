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
    Return 'C ' followed by the text from html request
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python/', default={'text': 'is cool'})
def python_text(text):
    """
    Return 'Python ' followed by text from html request with default
    text 'is cool'
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """
    Return html containing the number 'n'
    """
    return "{} is a number".format(n)

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
    parity = "even" if n % 2 == 0 else "odd"
    return render_template('odd_or_even.html', n=n, parity=parity)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
