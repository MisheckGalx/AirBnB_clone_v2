#!/usr/bin/python3
"""A Flask web application to display a list of states"""

# Import necessary modules
from flask import Flask, render_template
from models import storage
from models.state import State  # Import State model from models

# Create a Flask web application instance
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Route to display a list of states"""
    # Retrieve all State objects from the storage
    state_objs = storage.all(State)

    # Render a template ('7-states_list.html') with the retrieved state objects
    return render_template('7-states_list.html', state_objs=state_objs)


@app.teardown_appcontext
def teardown_db(exception):
    """Function to remove the current SQLAlchemy Session after each request"""
    storage.close()  # Close the SQLAlchemy session


# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
