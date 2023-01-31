# Import libraries
from flask import Flask, render_template, request, redirect
from cs50 import SQL
import subprocesses
from time import *

# Run the webscrapping function form file subprocesses
output_table_SB = subprocesses.webscrap()
sleep(1)

# Run sqlite_database function
subprocesses.sqlite_database(output_table_SB)

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///sqlite_database.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Define the home route along with other routes needed
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/tips")
def tips():
    return render_template("tips.html")

@app.route("/available_initial")
def available_initial():
    return render_template("available_initial.html")

@app.route("/available", methods=['POST', 'GET'])
def available():
    # SQL select statement to populate the html table with the data from the table "apartments"
    flats = db.execute("SELECT District, Address, Number_rooms, Area, Rent, Website FROM apartments")
    return render_template("available.html", database=flats, count=1)


