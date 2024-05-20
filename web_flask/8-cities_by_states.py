#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """
    Display a html page with states and cities.
    """
    states = storage.all(State)
    states_list = list(states.values())
    return render_template('8-cities_by_states.html', states=states_list)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove current session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
