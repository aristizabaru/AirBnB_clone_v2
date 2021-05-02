# #!/usr/bin/python3
"""7-states_list.py"""

from flask import Flask, render_template
from models import storage
from models.state import State


def main():
    """run web app"""
    app = Flask(__name__)

    @app.teardown_appcontext
    def teardown_db(error):
        storage.close()

    @app.route('/states_list', strict_slashes=False)
    def state_list():
        states = storage.all(State).values()
        states = sorted(states, key=lambda state: state.name)
        return render_template('7-states_list.html', states=states)

    app.run(host='0.0.0.0', port='5000')


if __name__ == '__main__':
    main()
