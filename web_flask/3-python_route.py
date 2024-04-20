#!/usr/bin/python3
"""2-c_route module"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """/: display “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """/hbnb: display “HBNB”"""
    return "HBNB"


# Route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display 'C <text>' where <text> is a URL parameter.
    Replaces underscores with spaces in <text>.
    """
    formatted_text = text.replace('_', ' ')

    return f"C {formatted_text}"

# Routes for '/python', '/python/' and '/python/<text>'
@app.route('/python', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """
    D 'Python <text>' where <text> is a URL parameter (default is 'is cool').
    Replaces underscores with spaces in <text>.
    """
    formatted_text = text.replace('_', ' ')
    return f"Python {formatted_text}"

# Check if this script is being run directly by the Python interpreter
if __name__ == '__main__':
    # Run the Flask application in debug mode on the local development server
    app.run(debug=True)
