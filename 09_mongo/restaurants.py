#Tiffany Cao & Kenneth Chin & Yaru Luo
#SoftDev2 pd1
#K09: Yummy Mongo Py
#2020-02-26

from bson.json_util import loads
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.restaurants

db.catalog.drop()  #clear everything in the collection first
catalog = db.catalog
with open("primer-dataset.json", "r") as file:
  content = file.readlines()
  for line in content:
    catalog.insert_one(loads(line))

def findBorough(borough):
  '''All restaurants in a specified borough'''
  results = catalog.find({ "borough": borough })
  print("Borough: {}".format(borough))
  print("Results Found: {}".format(results.count()))
  print() 
  for x in results:
    print(x["name"])

#findBorough("Queens")

def findZip(zip):
  '''All restaurants in a specified zipcode'''
  results = catalog.find({ "address.zipcode": zip })
  print("Zipcode: {}".format(zip))
  print("Results Found: {}".format(results.count()))
  print()
  for x in results:
    print(x["name"])

findZip("11355")
