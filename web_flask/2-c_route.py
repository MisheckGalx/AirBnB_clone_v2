#!/usr/bin/python3
"""2-c_route module"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """/: display “Hello HBNB!”"""
    return "Hello HBNB!"


# Define a route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """/hbnb: display “HBNB”"""
    return "HBNB"


# Define a route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display 'C <text>' where <text> is a URL parameter.
    Replaces underscores with spaces in <text>.
    """
    # Replace underscores in <text> with spaces
    formatted_text = text.replace('_', ' ')

    # Return the formatted text prefixed with 'C '
    return f"C {formatted_text}"

# Check if this script is being run directly by the Python interpreter
if __name__ == '__main__':
    # Run the Flask application in debug mode on the local development server
    app.run(debug=True)
