#!/usr/bin/python3
"""Flask web application with routes for text and rendering HTML templates"""


from flask import Flask, abort, render_template


app = Flask(__name__)


# Route for the root URL '/'
@app.route('/', strict_slashes=False)
def root():
    """Display 'Hello HBNB!' when accessing the root URL"""
    return "Hello HBNB!"


# Route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' when accessing the '/hbnb' URL"""
    return "HBNB"


# Route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display 'C <text>' where <text> is a URL parameter."""
    text_with_spaces = text.replace('_', ' ')
    return f"C {text_with_spaces}"


# Routes for '/python', '/python/', and '/python/<text>'
@app.route('/python', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """python_text: display Python and the text"""
    text_with_spaces = text.replace('_', ' ')

    return f"Python {text_with_spaces}"


# Route for '/number/<n>'
@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """Display '<n> is a number' only if <n> is an integer"""
    try:
        n = int(n)
        return f"{n} is a number"
    except ValueError:
        abort(404)


# Route for '/number_template/<n>'
@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """Display an HTML page (5-number.html)"""
    try:
        n = int(n)
        return render_template('5-number.html', n=n)
    except ValueError:
        abort(404)


# Route for '/number_odd_or_even/<n>'
@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display an HTML page (6-number_odd_or_even.html)"""
    try:
        n = int(n)
        odd_or_even = 'Odd' if n % 2 != 0 else 'Even'
        return render_template('6-number_odd_or_even.html', n=n)
    except ValueError:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
