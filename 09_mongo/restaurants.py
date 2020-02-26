#Tiffany Cao & Yaru Luo
#SoftDev1 pd1
#K12: Echo Echo Echo
#2019-09-26

from flask import Flask, render_template, request
import pymongo
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    print("hello")
    return "hello world"

@app.route("/") #route for landing page
def test_tmplt():
    # print(app)
    return render_template('form.html')




if __name__ == "__main__":
    app.debug = True
    app.run()
