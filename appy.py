from flask import Flask, render_template
import random
app = Flask(__name__)

## A list with total % * 10 entries, each occupation has its percentage * 10 entries
occupations10 = []

## list of occupations with percentages attached
occupations = []

## function to load the information from the file
def load_file(filename):
    with open (filename, 'r') as f:
        ## Read fileand make a list
        fstr = f.read()
        list_split = fstr.split('\n')
        heading = list_split[0]
        list_split = list_split[1:len(list_split) - 1]
        temp = []
        ## Accounting for occupations with commas in them
        for item in list_split:
            if item[0] == '"':
                temp2 = []
                temp2.append(item[1:item.index('"', 1)])
                temp2.append(float(item[item.index('",', 1) + 2 :])) ## adding percentages and converting to float
                temp.append(temp2)
            else:
                temp.append(item.split(","))
                temp[len(temp) - 1][1] = float(temp[len(temp) - 1][1])
        global occupations
        occupations = temp[:len(temp) - 2]

## Add occupations by their percentages ex:6.1% becomes 61 entries
def load_occupations():
    for item in occupations:
        for i in range(int(item[1] * 10)):
            occupations10.append(item[0])
    #print occupations10

## returns random element from occupations10
def get_random():
    return occupations10[random.randint(0,len(occupations10) - 1)]

load_file("occupations.csv")
load_occupations()
rand_occ = get_random()

@app.route("/occupations")
def occupy():
    return render_template('template.html', occA = rand_occ, arr_occ = occupations)

if __name__ == "__main__":
    app.debug = True
    app.run()
