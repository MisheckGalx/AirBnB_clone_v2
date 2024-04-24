#!/usr/bin/python3
"""A Flask web application to dynamically display content for an Airbnb clone"""

# Import necessary modules
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

# Create a Flask web application instance
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route to display dynamic content for the Airbnb clone"""
    # Retrieve all necessary objects from the database
    state_obj = storage.all(State)
    city_obj = storage.all(City)
    amenity_obj = storage.all(Amenity)
    place_obj = storage.all(Place)

    # Render a template ('100-hbnb.html') with retrieved objects
    return render_template(
        '100-hbnb.html',
        state_obj=state_obj,
        city_obj=city_obj,
        amenity_obj=amenity_obj,
        place_obj=place_obj
    )


@app.teardown_appcontext
def teardown_db(exception):
    """Function to remove the current SQLAlchemy Session after each request"""
    storage.close()  # Close the SQLAlchemy session


# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
