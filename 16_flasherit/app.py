# Tiffany Cao & Amanda Chen
# SoftDev1 pd1
# K16 -- Oh yes, perhaps I do…
# 2019-10-03

from flask import Flask, render_template, request, redirect, url_for, session, flash
app = Flask(__name__)


name = "Team Egg Fried Rice Period 1"
roster = "Amanda Chen & Tiffany Cao"
username = "Eggs"
password = "friedrice"

app.secret_key = "abcd"

@app.route("/")

def login():
    print(app)
    if 'user' in session: #keeps user logged in
         return redirect (url_for("welcome"))
    else: #for new user
        flash("Please log in.")
        return render_template('login.html',
                                team = name,
                                rost = roster)

@app.route("/welcome")
def welcome(): #welcome page for users that are logged in
    print(app)
    return render_template('welcome.html',
                            team = name,
                            rost = roster,
                            name = session['user'])

@app.route("/logout")
def logout(): #logout page redirected from logout button on welcome page
    print(app)
    session.pop('user') #removes session info
    flash("You have successfully logged out.")
    return render_template('logout.html', #back button goes back to login
                            team = name,
                            rost = roster)

@app.route("/auth")
def authenticate(): #checks to match user and pass
    print(url_for("login"))
    session['user'] = request.args['username']
    print(session['user'])
    if (request.args['username'] == username and request.args['password'] == password) :
       return redirect (url_for("welcome")) #goes to welcome page if credentials are correct
    else:
       return redirect (url_for("err")) #goes to error page is wrong


@app.route("/error") #error page
def err():
    print(request.form)
    if (session['user'] != username): #checks type of error
        flash("Username does not exist. Try again.")
    else:
        flash("Password does not match Username. Try again.")
    session.pop('user')
    return render_template('error.html', #back button goes back to login
                            team = name,
                            rost = roster)


if __name__ == "__main__":
    app.debug = True
    app.run()
