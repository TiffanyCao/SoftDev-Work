#Tiffany Cao & Emory Walsh
#SoftDev1 pd1
#K10 -- Jinja Tuning
#2019-09-20

import random
from flask import Flask, render_template
app = Flask(__name__)


#testing for normal route
@app.route("/")
def norm():
    return "normal"

coll = [0, 1, 1, 2, 3, 5, 8]

#setup for reading in the file and creating a dictionary
dict = {}
file = open("occupations.csv", "r")
content = file.readlines() #parse through file by lines
firstLine = content[0] #take out the first line for table title
firstLine = firstLine.split(",")
lastLine = content[len(content) - 1] #take out the last line for table end
lastLine = lastLine.split(",")
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

dict2 = {}
file2 = open("occupationsLinks.csv",  "r") #opens second file with links
content2 = file2.readlines() #parse through files by line
firstTitle = content2[0] #get the first line
firstTitle = firstTitle.split(",") #split the first line by the comma to get "Job" and "Link"
for line in content2:
    line = line.strip() #removes \n
    line = line.lstrip('\"') #removes leading quotation
    if ("\"" in line): #if line contains quotation marks
        line = line.split("\",") #splits line by ",
    else:
        line = line.split(",") #if line does not contain quotes, split by comma

    dict2[line[0]] = (line[1]) #key value pair
#print(dict) #testing results
file2.close()

#a function that gets a random job with the chances based on its percentage
def randJob():
    list = []
    for key, value in dict.items(): #found this iteration on stack overflow
        list += [key] * int(value * 10) #big thanks to Grace for this alternative to a forward loop
    #print(list)
    #print(len(list)) #should return 998
    return random.choice(list)

@app.route('/occupyflaskst')

#sets up html table structure by assigning the variables
def occs_template():
    #print(randJob())
    return render_template('tmplt.html',
        ti = "Occupations",
        randJob = randJob(),
        tableTitle1 = firstLine[0],
        tableTitle2 = firstLine[1],
        collection = dict, #percentages
        tableEnd1 = lastLine[0],
        tableEnd2 = float(lastLine[1]),
        linkTitle = firstTitle[1],
        linkColl = dict2 #links
        )


if __name__ == "__main__":
    app.debug = True
    app.run()
