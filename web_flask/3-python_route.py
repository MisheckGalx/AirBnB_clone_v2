#!/usr/bin/python3
"""2-c_route module"""

from flask import Flask

app = Flask(__name__)

# Route for the root URL '/'
@app.route('/', strict_slashes=False)
def root():
    """Display 'Hello HBNB!' when accessing the root URL"""
    return "Hello HBNB!"

# Route for '/hbnb'
@app.route('/', strict_slashes=False)
def root():
    """/: display “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    'C <text>' where <text> is a URL parameter.
    """
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"

# Routes for '/python', '/python/' and '/python/<text>'
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
