#!/usr/bin/python3
"""9-states.py"""

from flask import Flask, render_template
from models import storage
from models.state import State


def main():
    """run web app"""
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.teardown_appcontext
    def teardown_db(error):
        storage.close()

    @app.route('/states')
    def state_list():
        states = storage.all(State)
        return render_template('9-states.html', states=states)

    @app.route("/states/<param>")
    def states_id(param):
        for state in storage.all(State).values():
            if state.id == param:
                return render_template("9-states.html", state_id=state)
        return render_template("9-states.html")


if __name__ == '__main__':
    main()
