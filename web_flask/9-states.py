#!/usr/bin/python3
"""
Script that starts a Flaskweb application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    states = storage.all(State).values()
    states = sorted(states, key=lambda state; state.name)
    return render_template('states.html', states=states)


@app.route('/states/')
@app.route('/states/<id>')
def states_cities(id):
    """
    Display list of all the states
    """
    state = storage.all(State).get(f"State.{id}")
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('state.html', state=state, cities=cities)
    else:
        return render_template('state.html', state=None)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove current session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
