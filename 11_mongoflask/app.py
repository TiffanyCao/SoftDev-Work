#Amanda Zheng, Tiffany Cao, Team Blank
#K10 -- Import/Export Bank
#K11 --
#2020-03-05
from flask import Flask, render_template, request, session, redirect
# from pymongo import MongoClient
import json

# client = MongoClient("localhost", 27017)
# anime = client.weeb.anime
# anime.drop()
# file = open("anime-offline-database.json", "r")
# doc = json.load(file)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def form():
    check = request.args.get('search')
    print(check)
    if check is None:
        return render_template("home.html", tags = False)
    else:
        return render_template("home.html", tags = True)

# @app.route("/search", methods=['GET'])
# def search():
#     return render_template("home.html", tags = True)

@app.route("/results", methods=['GET'])
def start():
    if request.args.get('ova') or request.args.get('movie') or request.args.get('special'):
        return render_template("results.html")
    else:
        return redirect('error')
def finished():
    li=[]
    for x in anime.find({"status": "FINISHED"}):
        li.append(x["title"])
    return render_template("results.html", collection=li)
def rec():
    all=[]
    li=[]
    for x in anime.find({{},{"title":1} }):
        all.append(x["title"]) #easier way??
    for x in range(10):
        n=random.randint(0,len(all)-1)
        if n not in num:
            num.append(n)
            li.append(all[n])
    return render_template("results.html",collection=li)
def gallery():
    all=[]
    pic=[]
    li=[]
    for x in anime.find({{},{"title":1} }):
        all.append(x["title"]) #easier way??
        pic.append(x["picture"])
    return render_template("gallery.html",titles=all,pic=pic)

@app.route("/error", methods=['GET'])
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
