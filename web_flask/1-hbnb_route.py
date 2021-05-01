#!/usr/bin/python3
"""module 1-hbnb_route.py"""

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

    app.run(host='0.0.0.0', port='5000')


if __name__ == '__main__':
    main()
