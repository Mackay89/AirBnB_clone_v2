#!/usr/bin/python3
""" 
Script that starts a Flask web application that lists all states from DBStorage.
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/state_list')
def states_list():
    """
    Return the list of alll the states.
    """
    states = storage.all(State)
    states_list = list(states.values())
    return render_template('7-states_list.html', states=states_list)


@app.teardown_appcontext
def tearddown_db(exception):
    """
    Remove current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
