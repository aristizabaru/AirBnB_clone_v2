#!/usr/bin/python3
"""c_route.py"""

from flask import Flask


def main():
    """run web app"""
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def home():
        return 'Hello HBNB!'

    @app.route('/hbnb', strict_slashes=False)
    def hbnb():
        return 'HBNB'

    @app.route('/c/<text>', strict_slashes=False)
    def c_fun(text):
        text = text.replace('_', ' ')
        return 'C {}'.format(text)

    app.run(host='0.0.0.0', port='5000')


if __name__ == '__main__':
    main()
