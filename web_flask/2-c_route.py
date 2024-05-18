from flask import Flask

app = Flask(__name__)

@pp.route('/', strict_slashes=False)
def hellow_hbnb():
    return "Hello HBNB!"


@pp.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@pp.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return "C " + text.replace('_', ' ')


if __name__== "__main__":
    app.run(host='0.0.0.0', port=5000)
