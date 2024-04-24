#!/usr/bin/python3
"""A Flask web application to display states and their details"""

# Import necessary modules
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

# Create a Flask web application instance
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """Route to display state details based on state_id (optional)"""
    # Retrieve all State and City objects from the storage
    state_obj = storage.all(State)
    city_obj = storage.all(City)

    # Check if state_id is provided and exists in state_obj
    if state_id and f"State.{state_id}" in state_obj:
        state = state_obj[f"State.{state_id}"]
        # Render a template ('9-states.html') with state details
        return render_template(
            '9-states.html',
            state_obj=state_obj,
            state_id=state_id,
            city_obj=city_obj,
            state=state
        )

    # Render the template ('9-states.html') without specific state details
    return render_template(
        '9-states.html',
        state_obj=state_obj,
        state_id=state_id,
        city_obj=city_obj
    )


@app.teardown_appcontext
def teardown_db(exception):
    """Function to remove the current SQLAlchemy Session after each request"""
    storage.close()  # Close the SQLAlchemy session


# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
