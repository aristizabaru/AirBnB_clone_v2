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
    @app.route("/states/<id>", strict_slashes=False)
    def states_id(id=None):
        state_id = None
        states = None
        if id:
            for state in storage.all(State).values():
                if state.id == id:
                    state_id = state
        else:
            states = storage.all(State)
        return render_template("9-states.html", states=states, state_id=state_id)

    app.run(host='0.0.0.0', port='5000')


if __name__ == '__main__':
    main()
