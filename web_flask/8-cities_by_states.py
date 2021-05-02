#!/usr/bin/python3
"""8-cities_by_states.py"""

from flask import Flask, render_template
from models import storage
from models.state import State


def main():
    """run web app"""
    app = Flask(__name__)

    @app.teardown_appcontext
    def teardown_db(error):
        storage.close()

    @app.route('/cities_by_states', strict_slashes=False)
    def state_list():
        states = storage.all(State)
        return render_template('8-cities_by_states.html', states=states)

    app.run(host='0.0.0.0', port='5000')
