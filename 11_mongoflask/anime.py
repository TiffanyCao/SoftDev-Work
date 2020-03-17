#Amanda Zheng, Tiffany Cao, Team Blank
#K11 --
#2020-03-05

from flask import Flask, render_template, request,session
from pymongo import MongoClient
import json
from bson.json_util import loads

app = Flask(__name__)
client = MongoClient("localhost", 27017)
anime = client.weeb.anime

def create():
    anime.drop()
    file = open("anime.json", "r")
    doc = file.readlines()
    for x in doc:
        anime.insert_one(loads(x))

#create()

def findStatus(stat):
    if stat==0:
        return anime.find({})
    return anime.find({ "status": stat })

def findTitle(name):
    if name=="":
        return anime.find({})
    name=".*"+name+".*"
    #print(name)
    #print(anime.find({ "title": { "$regex": name, "$options": "i" }}).count())
    return anime.find({ "title": { "$regex": name, "$options" : "i" }})

def findEp(num,mode):
    if mode==0:
        return anime.find({})
    if(mode=="Less"):
        return anime.find({ "episodes": { "$lte": num }})
    else:
        return anime.find({ "episodes": { "$gte": num }})

def findType(type):
    if type==0:
        return anime.find({})
    #print(type)
    #print(anime.find({ "type": type }).count())
    return anime.find({ "type": type })

def findRand(num):
    return anime.aggregate([{ "$sample": { "size": num }}])

#for result in findStatus("CURRENTLY"):
    #if (result["title"]==""):
      #print("No Name Found")
    #else:
      #print (result["title"])

#for result in findTitle("girl"):
    #if (result["title"]==""):
      #print("No Name Found")
    #else:
      #print (result["title"])

#for result in findEp(20):
    #if (result["title"]==""):
      #print("No Name Found")
    #else:
      #print (result["title"])

#for result in findType("OVA"):
    #if (result["title"]==""):
      #print("No Name Found")
    #else:
      #print (result["title"])

#for result in findRand(10):
   #if (result["title"]==""):
     #print("No Name Found")
   #else:
     #print (result["title"])

if __name__ == "__main__":
    app.debug = True
    #app.run()
