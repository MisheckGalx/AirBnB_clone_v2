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
     """/c/<text>: display C and the text"""
    formatted_text = text.replace('_', ' ')

    return f"C {formatted_text}"

# Routes for '/python', '/python/' and '/python/<text>'
@app.route('/python', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """python_text: display Python and the text"""
    formatted_text = text.replace('_', ' ')

    return f"Python {formatted_text}"

if __name__ == '__main__':
    app.run(debug=True)
