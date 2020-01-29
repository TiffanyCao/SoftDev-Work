#Tiffany Cao & Yevgeniy Gorbachev
#SoftDev1 pd1
#K17 -- No Trouble
#2019-10-07

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >

# test SQL stmt in sqlite3 shell, save as string

command = "CREATE TABLE roster(name TEXT, age INTEGER, userid INTEGER PRIMARY KEY)" #create table named roster for students.csv
c.execute(command) #command executed
data = {}
with open('students.csv') as csvfile: #open and read students.csv file and store as dictionary
    data = csv.DictReader(csvfile)
    for row in data: #for every row in reader, insert values into roster table
         c.execute(f"INSERT INTO roster (name, age, userid) VALUES ('{row['name']}', {row['age']}, {row['id']})")

command2 = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)" #create table named courses for courses.csv
c.execute(command2) #command executed
data2 = {}
with open('courses.csv') as csvfile2: #open and read courses.csv file and store as dictionary
    data2 = csv.DictReader(csvfile2)
    for row in data2: #for every row in reader, insert values into courses table
        c.execute(f"INSERT INTO courses (code, mark, id) VALUES ('{row['code']}', {row['mark']}, {row['id']})")

#==========================================================

db.commit() #save changes
db.close()  #close database
