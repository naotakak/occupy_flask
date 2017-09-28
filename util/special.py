#Naotaka Kinoshita & Taylor Wong
#SoftDev1 pd7
#HW05 -- Jinja Tuning
#<2017>-<09>-<27>

import random

occupations = []
## function to load the information from the file
def load_file(filename):
    with open (filename, 'r') as f:
        ## Read file and make a list
        fstr = f.read()
        list_split = fstr.split('\n')
        list_split = list_split[1:len(list_split) - 1] #getting rid of first line
        temp_occ = [] #temporary list which will hold each line (ex: ["Occupation",6]) as a list (2D list)
        ## Accounting for occupations with commas in them
        for item in list_split:
            if item[0] == '"':
                comma_fix = [] #temporary list to account for the commas
                comma_fix.append(item[1:item.index('"', 1)])
                comma_fix.append(float(item[item.index('",', 1) + 2 :])) # adding percentages and converting to float
                temp_occ.append(comma_fix)
            else:
                temp_occ.append(item.split(","))
                temp_occ[len(temp_occ) - 1][1] = float(temp_occ[len(temp_occ) - 1][1]
        global occupations
        #occupations = []
        occupations = temp_occ[:len(temp_occ) - 2] #gets rid of last line ("Total...")
        return occupations

        
## Add occupations by their percentages ex:6.1% becomes 61 entries
def load_occupations(arr):
    occupations10 = []
    for item in arr:
        for i in range(int(item[1] * 10)):
            occupations10.append(item[0])
    return occupations10

    
## returns random element from occupations10
def get_random(arr):
    return random.choice(arr)