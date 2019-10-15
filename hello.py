# for windows use:
# set FLASK_APP=hello:app
# python -m flask run
# in the terminal
# REMEMBER! CAUTION WHEN PASTING CODE FROM SLACK, THE SPACES WILL BE AN ISSUE!

# import flask package. flask makes flask objects
from flask import Flask, render_template

#create Flask web server, makes the application
app = Flask(__name__)

#routes determine location
@app.route("/")

#Define simple function
def home():
    return render_template('home.html')

# Second route/page on the site
@app.route("/about")

def about():
    return render_template('about.html')

@app.route("/energy")

def energy():
    return render_template('energy.html')
