from bson.json_util import loads
from pymongo import MongoClient
import json

client = MongoClient("localhost", 27017)
anime = client.weeb.anime

def create():
    anime.drop()
    file = open("anime-offline-database.json", "r")
    doc = json.load(file)
    print("finished")
    print()

def finished():
    li=[]
    for x in anime.find({"status": "FINISHED"}):
        li.append(x["title"])
    print(li)

create()
finished()
