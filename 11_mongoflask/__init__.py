#Amanda Zheng, Tiffany Cao, Team Blank
#K11 -- Ay Mon Go Git It From Yer Flask
#2020-03-05
import os
from flask import Flask, render_template, request, session, redirect, flash, url_for
import anime

app = Flask(__name__)
app.secret_key = "help"

@app.route("/", methods=['GET', 'POST'])
def form():
    tags = False
    if request.form.get('search') is not None:
        tags = True
    return render_template("home.html", tags = tags)


@app.route("/results", methods=['GET', 'POST'])
def start():
   # print(request.form.get('supporttype'))
   # if request.form.get('supporttype') is not None:
   #   flash("Here " + request.form.get('supporttype'))
   #   return redirect(url_for('error'))
    if request.form.get('random') is not None or request.form.get('refresh') is not None:
      random = anime.findRand(10)
      return render_template("results.html", query = False, rand = True, random = random)
    if (request.args.get('findstuff') == "" and
       request.args.get('type') == "0" and
       request.args.get('status') == "0" and
       request.args.get('episodes') == "0"):
       flash("Please enter search queries.")
       return redirect(url_for('form'))
    search = "None"
    type = "None"
    status = "None"
    episodes = "None"
    if request.args.get('findstuff'): search = request.args.get('findstuff')
    if request.args.get('type') and request.args.get('type') != "0": type = request.args.get('type')
    if request.args.get('status') and request.args.get('status') != "0": status = request.args.get('status')
    if request.args.get('episodes') and request.args.get('episodes') != "0":
        episodes = request.args.get('episodes')
        if request.args.get('eps') == "":
            flash("Please enter a number for episodes.")
            return redirect(url_for('form'))
        elif int(request.args.get('eps')) < 0:
            flash("Please enter a valid episode number.")
            return redirect(url_for('form'))
        else:
            episodes += " " + request.args.get('eps') + " episode(s)"
    types=request.args.get("type")
    statuses=request.args.get("status")
    mode=request.args.get("episodes")
    ep=request.args.get("eps")
    title=request.args.get("findstuff")
    t=anime.findType(types)
    s=anime.findStatus(statuses)
    e=anime.findEp(ep,mode)
    h=anime.findTitle(title)
    loop=[]
    if(len(t)<len(s) and len(t)<len(e) and len(t)<len(h)):
        loop=t
    elif(len(s)<len(t) and len(s)<len(e) and len(s)<len(h)):
        loop=s
    elif(len(e)<len(s) and len(e)<len(t) and len(e)<len(h)):
        loop=e
    else:
        loop=h
    results = []
    count = 0
    for x in loop:
        if (x in s) and (x in t) and (x in e) and (x in h):
            results.append(x)
            count+=1
        if count>50:
            break
    # results.append(len(lengthT))
    # results.append(len(lengthE))
    # results.append(len(lengthS))
    # results.append(len(lengthH))
    return render_template("results.html", query = True, rand = False, search = search, type = type, status = status, episodes = episodes, results = results)

@app.route("/single", methods = ['GET', 'POST'])
def one():
    print(request.form.get('supporttype'))
    if request.form.get('supporttype') is not None:
      flash("Here " + request.form.get('supporttype'))
      return redirect(url_for('error'))
    return redirect(url_for('form'))

@app.route("/error", methods=['GET'])
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.debug = True
    anime.create()
    app.run()
