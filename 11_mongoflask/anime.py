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

def findTS(type, status):
    result = anime.find({ "type": type, "status": status })
    answer = []
    for x in result:
      answer.append(x['title'])
    print(len(answer))
    return answer

#print(findTS("OVA", "CURRENTLY"))

def findTSE(type, status, eps, mode):
    result = anime.find({ "type": type, "status": status, "episodes": { mode: eps }})
    answer = []
    for x in result:
      answer.append(x['title'])
    print(len(answer))
    return answer

#print(findTSE("OVA", "CURRENTLY", 0, "$lte"))

def all(type, status, eps, mode, title):
    if(type != "0" and status == "0" and mode == "0" and title == ""):
      result = findType(type)
    elif(type != "0" and status != "0" and mode == "0" and title == ""):
      result = anime.find({ "type": type, "status": status })
    #elif(type != "0" and status == "0" and mode == "0" 
    result = anime.find({ "type": type, "status": status, "episodes": { mode: eps }, "title": { "$regex": title, "$options" : "i" }})
    answer = []
    for x in result:
      answer.append(x['title'])
    print(len(answer))
    return answer

def test(type, status, mode, eps, title):
    t = []
    s = []
    if(type == "0"):
      t = ["OVA", "Movie", "Special", "ONA", "TV"]
    else:
      t.append(type)
    if(status == "0"):
      s = ["CURRENTLY", "UPCOMING", "FINISHED", "UNKNOWN"]
    else:
      s.append(status)
    if(title == ""):
      if(mode == "0"):
        result = anime.find({ "type": { "$in": t }, "status": { "$in": s }})
      else:
        result = anime.find({ "type": { "$in": t }, "status": { "$in": s }, "episodes": { mode: eps }})
    else:
      if(mode == "0"):
        result = anime.find({ "type": { "$in": t }, "status": { "$in": s }, "title": { "$regex": title, "$options" : "i" }})
      else:
        result = anime.find({ "type": { "$in": t }, "status": { "$in": s }, "episodes": { mode: eps }, "title": { "$regex": title, "$options" : "i" }})
    answer = []
    for x in result:
      answer.append(x['title'])
    print(len(answer))
    return answer

#for x in test("OVA", "CURRENTLY", "$lte", 0, ""):
#  print(x)

def findRand(num):
    return anime.aggregate([{ "$sample": { "size": num }}])

if __name__ == "__main__":
    app.debug = True
    #app.run()
