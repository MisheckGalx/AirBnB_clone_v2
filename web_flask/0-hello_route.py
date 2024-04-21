#!/usr/bin/python3
"""A simple Flask web application"""

from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL '/' of the web application
@app.route('/', strict_slashes=False)
def display():
    """Starts a Flask web application"""
    return 'Hello HBNB!'

# Check if this script is being run directly by the Python interpreter
if __name__ == '__main__':
    app.run(debug=True)
