

#create dictionary based on csv
dict = {} #initialize a new dictionary structure
file = open("occupations.csv", "r") #open up csv file for reading purposes
content = file.readlines() #parse through file by lines
content = content[1:len(content) - 1] #take out the first and last line
for line in content:
    print(line)
file.close()
