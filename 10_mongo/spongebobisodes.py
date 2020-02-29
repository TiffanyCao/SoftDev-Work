#Tiffany Cao & Ethan Chen
#SoftDev2 pd1
#K10: Import/Export Bank
#2020-02-29

from bson.json_util import loads
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.spongebob

info = db.info
with open("spongebob.json", "r") as file:  #read in json data
  content = file.readlines()
  if (info.count() == 0):
    for line in content:
      info.insert_one(loads(line))
    for x in info.find({}):
      #print(x)
      temp = x["_embedded"]["episodes"]
      for y in temp:
        db.episodes.insert_one(y)

def findEpisode(season, number):
  '''Episode name from the specified season and episode number.'''
  results = db.episodes.find({ "season": season, "number": number })
  print("Episode: {}  Number: {}".format(season, number))
  print("Results Found: {}".format(results.count()))
  for x in results:
    print(x["name"])

findEpisode(1, 1)
