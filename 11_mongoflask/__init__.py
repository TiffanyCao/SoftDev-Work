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
    # print("1" + request.args.get('findstuff'))
    # print(request.args.get('type'))
    # print(request.args.get('status'))
    # print(request.args.get('episodes'))
    # print("5" + request.args.get('eps'))
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
    return render_template("results.html", query = True, rand = False, search = search, type = type, status = status, episodes = episodes)

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