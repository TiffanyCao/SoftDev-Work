#Tiffany Cao
#SoftDev1 pd1
#K29 -- A RESTful Journey Skyward
#2019-11-12

from flask import Flask, render_template
import json
import urllib
app = Flask(__name__)

@app.route('/')
def root():
    u = urllib.request.urlopen(
    "https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=l0gJ0GCRc5FKMmNYD5gITEtP8dpfsz5FPc0nv8ok"
    )
    response = u.read()
    data = json.loads(response)
    # stuff = stuff['href']
    return render_template("index.html", pic = data['url'])


    # u = urllib.request.urlopen(
    # "https://images-api.nasa.gov/search?q=earth&nasa_id=PIA00122"
    # )
    # response = u.read()
    # data = json.loads(response)
    # stuff = data['collection']
    # stuff = stuff['items']
    # stuff = stuff[0]
    # stuff = stuff['links']
    # stuff = stuff[0]
    # stuff = stuff['href']
    # # stuff = stuff['href']
    # return render_template("index.html", pic = stuff)

if __name__ == "__main__":
    app.debug = True
    app.run()
