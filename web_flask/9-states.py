#!/usr/bin/python3
"""9-states.py"""

from flask import Flask, render_template
from models import storage
from models.state import State


def main():
    """run web app"""
    app = Flask(__name__)

    @app.teardown_appcontext
    def teardown_db(error):
        storage.close()

    @app.route('/states', strict_slashes=False)
    def state_list():
        states = storage.all(State)
        return render_template('9-states.html', states=states)

    @app.route('/states/<id>', strict_slashes=False)
    def state_id(id):
        states = storage.all(State)
        state_id = states['State.'+id]
        return render_template('9-states.html', state_id=state_id)

    app.run(host='0.0.0.0', port='5000')


if __name__ == '__main__':
    main()
