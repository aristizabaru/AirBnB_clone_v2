#!/usr/bin/python3
"""module 0-hello_route.py"""

from flask import Flask


def main():
    """run web app"""
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.route('/')
    def home():
        return 'Hello HBNB!'

    app.run(host='0.0.0.0', port='5000')


if __name__ == '__main__':
    main()
