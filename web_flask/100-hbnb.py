#!/usr/bin/python3
"""9-states.py"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


def main():
    """run web app"""
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.teardown_appcontext
    def teardown_db(error):
        storage.close()

    @app.route('/hbnb')
    def state_list():
        states = storage.all(State)
        amenities = storage.all(Amenity)
        places = storage.all(Place)
        return render_template('100-hbnb.html',
                               states=states,
                               amenities=amenities,
                               places=places)

    app.run(host='0.0.0.0', port='5000')


if __name__ == '__main__':
    main()
