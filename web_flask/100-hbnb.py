#!/usr/bin/python3
"""
Script that starts a Flask web application to display HBNB data
"""
from flask import Flask, render_template
from models import storage
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """
    close the SQLAlchemy session after each request.
    """
    storage.close()


@app.route('/hbnb')
def hbnb():
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    data= {
        'states': list(states.values()),
        'amenities': list(amenities.values()),
        'place': list(places.values())
     }
    return render_template('100-hbnb.html', **data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
