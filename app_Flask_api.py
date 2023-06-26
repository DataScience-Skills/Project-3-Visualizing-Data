##################################################################################################
##################################################################################################
##################################################################################################
# Make sure to replace 'username', 'password', and 'database_name' in the create_engine line with your PostgreSQL credentials.

# With this updated code, you can access the following routes:

# Home route: http://localhost:5000/
# Generators route: http://localhost:5000/api/v1.0/generators
# States route: http://localhost:5000/api/v1.0/states
# These routes will return the generator data and states data from the PostgreSQL database respectively, in JSON format.

# Remember to install the required dependencies (flask, sqlalchemy, and psycopg2 for PostgreSQL) using pip before running the application.
##################################################################################################
##################################################################################################
##################################################################################################
# ChatGPT prompted Flask API

# Import required modules and classes
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Create an instance of Flask
app = Flask(__name__)

# Create engine and reflect the database schema
engine = create_engine('postgresql://username:password@localhost:5432/database_name')
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to the tables in the database
Generators = Base.classes.Generators
States = Base.classes.States

# Create a session
session = Session(engine)

# Define the home route
@app.route('/')
def home():
    """List all available routes"""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/generators<br/>"
        f"/api/v1.0/states<br/>"
    )

# Define the generators route
@app.route('/api/v1.0/generators')
def get_generators():
    """Return the generator data"""
    results = session.query(Generators).all()

    # Create a list of dictionaries containing generator data
    generator_data = []
    for result in results:
        generator_dict = {
            'id': result.id,
            'period': result.period,
            'stateID': result.stateID,
            'sector': result.sector,
            'entityid': result.entityid,
            'plantid': result.plantid,
            'generatorid': result.generatorid,
            'technology': result.technology,
            'energy_source_code': result.energy_source_code,
            'prime_mover_code': result.prime_mover_code,
            'status': result.status,
            'latitude': result.latitude,
            'longitude': result.longitude
        }
        generator_data.append(generator_dict)

    # Return the JSON list of generator data
    return jsonify(generator_data)

# Define the states route
@app.route('/api/v1.0/states')
def get_states():
    """Return the states data"""
    results = session.query(States).all()

    # Create a list of dictionaries containing states data
    states_data = []
    for result in results:
        state_dict = {
            'stateID': result.stateID,
            'state_description': result.state_description
        }
        states_data.append(state_dict)

    # Return the JSON list of states data
    return jsonify(states_data)

if __name__ == '__main__':
    app.run(debug=True)
