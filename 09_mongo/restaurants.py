#Tiffany Cao & Kenneth Chin
#SoftDev2 pd1
#K09: Yummy Mongo Py
#2020-02-26

from flask import Flask, render_template, request
import pymongo
from pymongo import MongoClient
import json
app = Flask(__name__)

client = MongoClient("localhost", 27017)
db = client.restaurants

#db.inventory.insert_one(
#  {"address": {"building": "469", "coord": [-73.961704, 40.662942], "street": "Flatbush Avenue", "zipcode": "11225"}, "borough": "Brooklyn", "cuisine": "Hamburgers", "grades": [{"date": {"$date": 1419897600000}, "grade": "A", "score": 8}, {"date": {"$date": 1404172800000}, "grade": "B", "score": 23}, {"date": {"$date": 1367280000000}, "grade": "A", "score": 12}, {"date": {"$date": 1336435200000}, "grade": "A", "score": 12}], "name": "Wendy'S", "restaurant_id": "30112340"},{"address": {"building": "351", "coord": [-73.98513559999999, 40.7676919], "street": "West   57 Street", "zipcode": "10019"}, "borough": "Manhattan", "cuisine": "Irish", "grades": [{"date": {"$date": 1409961600000}, "grade": "A", "score": 2}, {"date": {"$date": 1374451200000}, "grade": "A", "score": 11}, {"date": {"$date": 1343692800000}, "grade": "A", "score": 12}, {"date": {"$date": 1325116800000}, "grade": "A", "score": 12}], "name": "Dj Reynolds Pub And Restaurant", "restaurant_id": "30191841"}
#)

results = db.catalog.find({ "borough" : "Manhattan" })[0]
print(results)

if __name__ == "__main__":
    app.debug = True
   #app.run()
