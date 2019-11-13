#Tiffany Cao
#SoftDev1 pd1
#K
#2019

from flask import Flask, render_template
import json
import urllib
app = Flask(__name__)

@app.route('/')
def root():
    return render_template("home.html")

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


if __name__ == "__main__":
    app.debug = True
    app.run()
