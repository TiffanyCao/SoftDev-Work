#Tiffany Cao & Jackie Lin
#SoftDev1 pd1
#K25 -- Getting More REST
#2019-11-13

from flask import Flask, render_template
import json
import urllib
app = Flask(__name__)

@app.route('/')
def root():
    return render_template("main.html")

@app.route('/addressautocomplete')
def address():
    u = urllib.request.urlopen(
    "https://us-autocomplete.api.smartystreets.com/suggest?auth-id=2676fc89-0bed-fde9-0ff6-b70829031c6c&auth-token=022h0rkvcmLqMZ7EXEii&prefix=4770%20Lincoln%20Ave%20O"
    )
    response = u.read()
    data = json.loads(response)
    data = data['suggestions']
    # stuff = stuff['href']
    return render_template("index1.html", stuff = data, length = len(data))

@app.route("/darksky")
def darksky():
    url = "https://api.darksky.net/forecast/28b607f4a70a742bd83b0931b1590466/42.3601,-71.0589"
    u = urllib.request.urlopen(url)
    response = u.read()
    data = json.loads(response)
    return render_template("darksky.html",lat=data['latitude'], long=data['longitude'], timezone=data['timezone'], time=data['currently']['time'], sum=data['currently']['summary'])


if __name__ == "__main__":
    app.debug = True
    app.run()
