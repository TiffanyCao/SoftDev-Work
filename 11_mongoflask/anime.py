#Amanda Zheng, Tiffany Cao, Team Blank
#K10 -- Import/Export Bank
#K11 --
#2020-03-05
from flask import Flask, render_template, request,session
from pymongo import MongoClient
import json
from bson.json_util import loads
client = MongoClient("localhost", 27017)
anime = client.weeb.anime
anime.drop()
file = open("anime.json", "r")
doc = file.readlines()
for x in doc:
    anime.insert_one(loads(x))

def findAnime(a):
    return anime.find( { "status": a },{ "name": 1,"_id":0} )

for result in findAnime("FINISHED"):
   print(result["title"])

app = Flask(__name__)

if __name__ == "__main__":
    app.debug = True
    app.run()
