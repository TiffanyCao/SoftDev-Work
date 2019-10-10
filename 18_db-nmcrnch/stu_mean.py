#Jesse "McCree" Chen
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#Part 1
command = "CREATE TABLE classData (courses TEXT, mark INTEGER, id INTEGER)" #create table named classData for courses.csv
c.execute(command)

csvfile = open('courses.csv') #open and read courses.csv file and store as dictionary
reader = csv.DictReader(csvfile)
for row in reader: #for every row in reader, insert values into classData table
	command = "INSERT INTO classData VALUES(\"" + row['code'] + "\"," + row['mark'] + "," + row['id'] + ")"
	c.execute(command)


command = "CREATE TABLE studentData (name TEXT, age INTEGER, id INTEGER)" #create table named studentData for students.csv
c.execute(command)

csvfile = open('students.csv') #open and read students.csv file and store as dictionary
reader = csv.DictReader(csvfile)
for row in reader: #for every row in reader, insert values into studentData table
	command = "INSERT INTO studentData VALUES(\"" + row['name'] + "\"," + row['age'] + "," + row['id'] + ")"
	c.execute(command)


#Part 2

def findID(tempName): #function that retrieves the ID of a student given their name, from the database
	#set cursor to find and list IDs with names tempName
	cur = c.execute(f"SELECT id FROM studentData WHERE name = '{tempName}'")
	return cur.fetchone()[0]

# testing
# print(findID("alison")) #10
# print(findID("TOKiMONSTA")) #7

def findGrades(tempName): #function that retrieves the courses and grades in those courses of a student given their name, from the database
	#set cursor to find and list the classes and the marks in those classes given name of student
	cur = c.execute(f"SELECT courses, mark FROM classData WHERE id = '{findID(tempName)}'")
	return cur.fetchall()

# testing
# print(findGrades("alison")) #[('systems', 85), ('softdev', 80)]
# print(findGrades("TOKiMONSTA")) #[('greatbooks', 70), ('systems', 88), ('softdev', 85)]

def findGrades2(tempName): #function that only retrieves the grades (and not the courses) of a student given their name, from the database
	#set cursor to find and list the classes and the marks in those classes given name of student
	cur = c.execute(f"SELECT mark FROM classData WHERE id = '{findID(tempName)}'")
	return cur.fetchall()

# testing
# print(findGrades2("alison")) #[(85,), (80,)]
# print(findGrades2("TOKiMONSTA")) #[(70,), (88,), (85,)]

def findAvg(tempName): #function that calculates the average of a student's grades given their name, from the database
	#set cursor to find the grades of a student given their name and put them in a list
	cur = c.execute(f"SELECT mark FROM classData WHERE id = '{findID(tempName)}'")
	avg = 0
	temp = cur.fetchall()
	length = 0
	#calculate the sum of grades
	for row in temp:
  		avg += row[0]
	#calculate the number of grades
	for row in temp:
		length += 1
	return avg / length

# testing
# print(findAvg("alison")) #82.5
# print(findAvg("TOKiMONSTA")) #81.0

def findAvgID(numID): #function that calculates the average of a student's grades given their ID, from the database
	#set cursor to find the grades of a student given their ID and put them in a list
	cur = c.execute(f"SELECT mark FROM classData WHERE id = '{numID}'")
	avg = 0
	temp = cur.fetchall()
	length = 0
	#calculate the sum of grades
	for row in temp:
  		avg += row[0]
	#calculate the number of grades
	for row in temp:
		length += 1
	return avg / length

# testing
# print(findAvgID(10)) #82.5
# print(findAvgID(7)) #81.0

def studentInfo(tempName): #function that retrieves the name, ID, and average grade of a student, given their name, from the database
	return "" + tempName + ", " + str(findID(tempName)) + ", " + str(findAvg(tempName))

# testing
# print(studentInfo("alison")) #alison, 10, 82.5
# print(studentInfo("TOKiMONSTA")) #TOKiMONSTA, 7, 81.0

command = "CREATE TABLE stu_avg (id INTEGER, average INTEGER)" #create table named stu_avg for the averages of the students
c.execute(command)

#set cursor to find and list all the IDs found in studentData table
cur = c.execute("SELECT id FROM studentData")
temp = cur.fetchall()
studentID = ""
for row in temp: #for every student, insert into stu_avg the values of their ID and average grade
	studentID = row[0]
	command = "INSERT INTO stu_avg VALUES("+ str(studentID) + ", " + str(findAvgID(studentID)) + ")"
	c.execute(command)

def addCourse(course, grade, studentID): #function that facilitates the addition of a new row into the classData/courses table, given the course, mark, and ID
	command = "INSERT INTO classData VALUES(\"" + course + "\", " + str(grade) + ", " + str(studentID) + ")"
	c.execute(command)

# testing
# addCourse("painting", 100, 11)
# addCourse("writing", 85, 11)
# addCourse("writing", 100, 7)
#
# print(findAvgID(7)) #85.75
#==========================================================

db.commit() #save changes
db.close()  #close database
