#Naotaka Kinoshita & Taylor Wong
#SoftDev1 pd7
#HW05 -- Jinja Tuning
#<2017>-<09>-<27>   

from flask import Flask, render_template
from util import special
app = Flask(__name__)

## A list with total % * 10 entries, each occupation has its percentage * 10 entries
occupations10 = []

## list of occupations with percentages attached
occupations = []

##use above functions specifically for occupations.csv file
occupations = special.load_file("data/occupations.csv")
occupations10 = special.load_occupations(occupations)

#create default route
@app.route("/")
def home():
    return "<a href='/occupations'>Occcupations</a>"


#create route to generate HTML page
@app.route("/occupations")
def occupy():
    return render_template('template.html', occA = special.get_random(occupations10), arr_occ = occupations)

if __name__ == "__main__":
    app.debug = True
    app.run()
