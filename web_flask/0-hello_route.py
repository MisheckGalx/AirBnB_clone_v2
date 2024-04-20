#!/usr/bin/python3
"""A simple Flask web application"""
from flask import Flask


app = Flask(__name__)

# Write a script that starts a Flask web application:
@app.route('/', strict_slashes=False)
def display():
    """Script that starts a Flask web application"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(debug=True)
