#!/usr/bin/python3
"""A simple Flask web application with multiple routes"""

from flask import Flask


app = Flask(__name__)


# Define a route for the root URL '/'
@app.route('/', strict_slashes=False)
def root():
    """/: Display 'Hello HBNB!' when accessing the root URL"""
    return "Hello HBNB!"


# Define a route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """/hbnb: Display 'HBNB' when accessing the '/hbnb' URL"""
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=True)
