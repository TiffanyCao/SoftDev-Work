import random

#create dictionary based on csv
dict = {} #initialize a new dictionary structure
file = open("occupations.csv", "r") #open up csv file for reading purposes
content = file.readlines() #parse through file by lines
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

#print(randJob())
