#Amanda Zheng, Tiffany Cao, Team Blank
#K11 -- Ay Mon Go Git It From Yer Flask
#2020-03-05
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
    if request.form.get('random') is not None:
        return render_template("results.html", query = False)
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
    return render_template("results.html", query = True, search = search, type = type, status = status, episodes = episodes)

# def finished():
#     li=[]
#     for x in anime.find({"status": "FINISHED"}):
#         li.append(x["title"])
#     return render_template("results.html", collection=li)
# def rec():
#     all=[]
#     li=[]
#     for x in anime.find({{},{"title":1} }):
#         all.append(x["title"]) #easier way??
#     for x in range(10):
#         n=random.randint(0,len(all)-1)
#         if n not in num:
#             num.append(n)
#             li.append(all[n])
#     return render_template("results.html",collection=li)
# def gallery():
#     all=[]
#     pic=[]
#     li=[]
#     for x in anime.find({{},{"title":1} }):
#         all.append(x["title"]) #easier way??
#         pic.append(x["picture"])
#     return render_template("gallery.html",titles=all,pic=pic)

# @app.route("/error", methods=['GET'])
# def error():
#     return render_template("error.html")

if __name__ == "__main__":
    app.debug = True
    anime.create()
    app.run()
