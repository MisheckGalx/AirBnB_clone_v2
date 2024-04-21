#!/usr/bin/python3
"""A Flask web application with multiple routes"""

from flask import Flask


app = Flask(__name__)


# Define a route for the root URL '/'
@app.route('/', strict_slashes=False)
def root():
    """Display 'Hello HBNB!' when accessing the root URL"""
    return "Hello HBNB!"


# Define a route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' when accessing the '/hbnb' URL"""
    return "HBNB"


# Define a route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display 'C <text>' where <text> is a URL parameter.
    """
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"


# Define routes for '/python', '/python/' and '/python/<text>'
@app.route('/python', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """
		'Python <text>' where <text> is a URL parameter (default is 'is cool').
    """
    formatted_text = text.replace('_', ' ')
    return f"Python {formatted_text}"


if __name__ == '__main__':
    app.run(debug=True)
