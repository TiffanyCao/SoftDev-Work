#Team Eggcellent: Tiffany Cao & Ethan Chen
#SoftDev2 pd1
#K10: Import/Export Bank
#2020-02-29

from bson.json_util import loads
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.eggcellent 

#The data bank used was the Spongebob Squarepants Episode dataset from TV Maze API
#This file provides numerous details about every SBSP episode in all the seasons, including episode summary, airtime, airdate, and more.
#The link to the API is: http://www.tvmaze.com/api
#The link to the JSON file for Spongebob Squarepants episodes is: http://api.tvmaze.com/singlesearch/shows?q=spongebob-squarepants&embed=episodes

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
  #formatting printed results
  print("Season: {}  Episode: {}".format(season, number))
  print("Results Found: {}".format(results.count()))
  print()
  for x in results:
    print("Episode Title: {}".format(x["name"]))
    if(x["summary"] == "" or x["summary"] is None):
      print("No summary available.")
    else:
      print(x["summary"][3:-4] + "\n")

findEpisode(1, 1)

def findSeason(season):
  '''All episodes from specified season.'''
  results = db.episodes.find({ "season": season })
  #formatting printed results
  print("Season: {}".format(season))
  print("Results Found: {}".format(results.count()))
  print()
  for x in results:
    print("Episode {}:  {}".format(x["number"], x["name"]))
    if(x["summary"] == "" or x["summary"] is None):
      print("No summary available." + "\n")
    else:
      print(x["summary"][3:-4] + "\n")

findSeason(1)
findSeason(2)

def onAir(airdate):
  '''Episode from the specified airing date.'''
  results = db.episodes.find({ "airdate": airdate })
  #formatting printed results
  print("Given Date: {}".format(airdate))
  print("Results Found: {}".format(results.count()))
  print()
  for x in results:
    print("Season {} Episode {}: {}".format(x["season"], x["number"], x["name"]))
    if(x["summary"] == "" or x["summary"] is None):
      print("No summary available." + "\n")
    else:
      print(x["summary"][3:-4] + "\n")

onAir("2001-03-06")

def findWords(key):
  keyword = ".*" + key + ".*"
  results = db.episodes.find({"summary": {"$regex": keyword }})
  #formatting printed results
  print("Key Word: {}".format(key))
  print("Results Found: {}".format(results.count()))
  print()
  for x in results:
    print("Season: {}  Episode: {}".format(x["season"], x["number"]))
    print("Episode Title: {}".format(x["name"]))
    print(x["summary"][3:-4] + "\n")

findWords("Sandy Cheeks")
findWords("Squidward")
