#!/usr/bin/python3
"""
Scriptthat starts a Flask web application.
"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_route1():
    """
    Display 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_route2():
    """
    Display 'HBNB'
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_route3(text):
    """
    Display 'C ' followed by the text from html request
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def hello_route4(text):
    """
    Display 'Python ' followed by text from html request with 
    default text 'is cool'
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def hello_route5(n):
    """
    Display last part of html request formatted as a number if it can
    be converted to an int.
    """
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>')
def hello_route6(n):
    """
    Display html template containing the number 'n'
    """
    return render_template('5-number.html', number=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
