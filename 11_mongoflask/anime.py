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
        result= anime.find({})
    else:
        result= anime.find({ "status": stat })
    answer=[]
    for x in result:
        answer.append(x["title"].encode('utf8'))
    return answer

def findTitle(name):
    if name=="":
        result= anime.find({})
    else:
        name=".*"+name+".*"
        result= anime.find({ "title": { "$regex": name, "$options" : "i" }})
    answer=[]
    for x in result:
        answer.append(x['title'].encode('utf8'))
    return answer

def findEp(num,mode):
    if mode==0 or num == "":
        result= anime.find({})
    if(mode=="Less"):
        result= anime.find({ "episodes": { "$lte": num }})
    else:
        result= anime.find({ "episodes": { "$gte": num }})
    answer=[]
    for x in result:
        answer.append(x['title'].encode('utf8'))
    return answer


def findType(type):
    if type==0:
        result=anime.find({})
    else:
        result= anime.find({ "type": type })
    answer=[]
    for x in result:
        answer.append(x['title'].encode('utf8'))
    return answer

def findRand(num):
    return anime.aggregate([{ "$sample": { "size": num }}])

if __name__ == "__main__":
    app.debug = True
    #app.run()
