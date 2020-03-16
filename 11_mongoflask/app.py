#Amanda Zheng, Tiffany Cao, Team Blank
#K11 -- Ay Mon Go Git It From Yer Flask
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

@app.route("/", methods=['GET', 'POST'])
def form():
    tags = False
    list = False
    find = False
    check = request.form.get('search')
    check2 = request.form.get('list')
    check3 = request.form.get('find')
    if check is not None:
        tags = True
    if check2 is not None:
        list = True
    if check3 is not None:
        find = True
    return render_template("home.html", tags = tags, list = list, find = find)


@app.route("/results", methods=['GET', 'POST'])
def start():
    if request.args.get('ova') or request.args.get('movie') or request.args.get('special'):
        li = []
        if request.args.get('ova'): li.append("OVA")
        if request.args.get('movie'): li.append("Movie")
        if request.args.get('special'): li.append("Special")
        return render_template("results.html", search = li, list = True, length = len(li))
    elif request.args.get('findstuff'):
        print(request.args.get('findstuff'))
        return render_template("results.html", search = request.args.get('findstuff'), list = False)
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
