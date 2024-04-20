#!/usr/bin/python3
"""A simple Flask web application"""


from flask import Flask


app = Flask(__name__)

# Define a route for the root URL '/' of the web application
@app.route('/', strict_slashes=False)
def display():
    """Display 'Hello HBNB!' when accessing the root URL"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(debug=True)
