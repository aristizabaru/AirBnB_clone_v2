#!/usr/bin/python3
"""5-number_template.py"""

from flask import Flask, render_template


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

    @app.route('/python', strict_slashes=False)
    @app.route('/python/<text>', strict_slashes=False)
    def python(text='is cool'):
        text = text.replace('_', ' ')
        return 'Python {}'.format(text)

    @app.route('/number/<int:n>', strict_slashes=False)
    def number(n):
        return '{} is a number'.format(n)

    @app.route('/number_template/<int:n>', strict_slashes=False)
    def number_template(n):
        return render_template('5-number.html', number=n)

    app.run(host='0.0.0.0', port='5000')


if __name__ == '__main__':
    main()
