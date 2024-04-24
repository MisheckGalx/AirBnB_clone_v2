#!/usr/bin/python3
"""A Flask web application to display cities grouped by states"""

# Import necessary modules
from flask import Flask, render_template
from models import storage
from models.state import State  # Import State model
from models.city import City  # Import City model

# Create a Flask web application instance
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Route to display states and their associated cities"""
    # Retrieve all State and City objects from the storage
    states = storage.all(State)
    cities = storage.all(City)

    # Render a template ('8-cities_by_states.html') with the retrieved objects
    return render_template(
        '8-cities_by_states.html',
        states=states,
        cities=cities
    )


@app.teardown_appcontext
def teardown_db(exception):
    """Function to remove the current SQLAlchemy Session after each request"""
    storage.close()  # Close the SQLAlchemy session


# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
