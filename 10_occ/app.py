#Tiffany Cao & Emory Walsh
#SoftDev1 pd1
#K10 -- Jinja Tuning
#2019-09-20

import random
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def norm():
    return "normal"

coll = [0, 1, 1, 2, 3, 5, 8]


#def norm():
#    return "Go to other page"

dict = {}
file = open("occupations.csv", "r")
content = file.readlines() #parse through file by lines
firstLine = content[0]
lastLine = content[len(content) - 1]
content = content[1:len(content) - 1] #take out the first and last line
for line in content:
    line = line.strip() #removes \n
    line = line.lstrip('\"') #removes leading quote
    if ("\"" in line): #if line contains quotation marks
        line = line.split("\",") #splits line by ",
    else:
        line = line.split(",") #if line does not contain quotes, split by comma

    dict[line[0]] = float(line[1]) #key value pair
#print(dict) #testing results
file.close()

def randJob():
    list = []
    for key, value in dict.items(): #found this iteration on stack overflow
        list += [key] * int(value * 10) #big thanks to Grace for this alternative to a forward loop
    #print(list)
    #print(len(list)) #should return 998
    return random.choice(list)

@app.route('/occupyflaskft')

def occs_template():
    #print(randJob())
    return render_template('tmplt.html',
        ti = "Occupations",
        randJob = randJob(),
        tableTitle = firstLine,
        collection = dict,
        tableEnd = lastLine
        #collection = dict

        )


if __name__ == "__main__":
    app.debug = True
    app.run()
