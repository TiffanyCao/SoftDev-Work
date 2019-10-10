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
command = "CREATE TABLE classData (courses TEXT, mark INTEGER, id INTEGER)"
c.execute(command)

csvfile = open('courses.csv')
reader = csv.DictReader(csvfile)
for row in reader:
	command = "INSERT INTO classData VALUES(\"" + row['code'] + "\"," + row['mark'] + "," + row['id'] + ")"
	c.execute(command)


command = "CREATE TABLE studentData (name TEXT, age INTEGER, id INTEGER)"
c.execute(command)

csvfile = open('students.csv')
reader = csv.DictReader(csvfile)
for row in reader:
	#print(row)
	command = "INSERT INTO studentData VALUES(\"" + row['name'] + "\"," + row['age'] + "," + row['id'] + ")"
	c.execute(command)


#Part 2
def findID(tempName):
	cur = c.execute(f"SELECT id FROM studentData WHERE name = '{tempName}'")
	#temp = cur.fetchone()[0]
	return cur.fetchone()[0]

print(findID("alison"))

def findGrades(tempName):
	#set cursor to find grades of student with given name
	cur = c.execute(f"SELECT courses, mark FROM classData WHERE id = '{findID(tempName)}'")
	return cur.fetchall()

print(findGrades("alison"))

def findAvg(tempName):
	cur = c.execute(f"SELECT mark FROM classData WHERE id = '{findID(tempName)}'")
	avg = 0
	temp = cur.fetchall()
	length = 0
	for row in temp:
  		avg += row[0]
	for row in temp:
		length += 1
	#print(length)
	return avg / length

print(findAvg("alison"))

def findAvgID(numID):
	cur = c.execute(f"SELECT mark FROM classData WHERE id = '{numID}'")
	avg = 0
	temp = cur.fetchall()
	length = 0
	for row in temp:
  		avg += row[0]
	for row in temp:
		length += 1
	#print(length)
	return avg / length

print(findAvgID(10))

def studentInfo(tempName):
	return "" + tempName + ", " + str(findID(tempName)) + ", " + str(findAvg(tempName))

print(studentInfo("alison"))

command = "CREATE TABLE stu_avg (id INTEGER, average INTEGER)"
c.execute(command)

cur = c.execute("SELECT id FROM studentData")
temp = cur.fetchall()
studentID = ""
for row in temp:
	studentID = row[0]
	command = "INSERT INTO stu_avg VALUES("+ str(studentID) + ", " + str(findAvgID(studentID)) + ")"
	c.execute(command)

#==========================================================

db.commit() #save changes
db.close()  #close database
