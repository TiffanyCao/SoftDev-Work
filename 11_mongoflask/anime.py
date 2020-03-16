#Amanda Zheng, Tiffany Cao, Team Blank
#K10 -- Import/Export Bank
#K11 --
#2020-03-05
from flask import Flask, render_template, request,session
from pymongo import MongoClient
import json
from bson.json_util import loads

app = Flask(__name__)

def create():
    client = MongoClient("localhost", 27017)
    anime = client.weeb.anime
    anime.drop()
    file = open("anime.json", "r")
    doc = file.readlines()
    for x in doc:
        anime.insert_one(loads(x))

def findStatus(stat):
    return anime.find({ "status": stat })

def findTitle(name):
    name=".*"+name+".*"
    return anime.find({ "title": { "$regex": name, "$options" : "i" }})

def findEp(num):
    return anime.find({ "episodes": { "$lte": num }})

def findType(type):
    return anime.find({ "type": type })

for result in findStatus("CURRENTLY"):
    if (result["title"]==""):
        print("No Name Found")
    else:
      print (result["title"])

for result in findTitle("girl"):
    if (result["title"]==""):
        print("No Name Found")
    else:
      print (result["title"])

for result in findEp(20):
    if (result["title"]==""):
        print("No Name Found")
    else:
      print (result["title"])

for result in findType("OVA"):
    if (result["title"]==""):
        print("No Name Found")
    else:
      print (result["title"])


if __name__ == "__main__":
    app.debug = True
    app.run()
