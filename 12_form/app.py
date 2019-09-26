#Tiffany Cao & Yaru Luo
#SoftDev1 pd1
#K
#2019

from flask import Flask, render_template, request
import cgi

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("hello")
    return "hello world"

@app.route("/forms")
def test_tmplt():
    print(app)
    return render_template('form.html')


# @app.route("/auth")
# def authenticate():
#     print(app)
#     print(request)
#     print(request.args)
#     print(request.args['username'])
#     print(request.headers)
#     return render_template('response.html',
#         name = request.args['username'])


@app.route("/auth")
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username'] ***)
    #print(request.args['username'] #only works if username submitted
    #print("***DIAG: request.headers ***)
    #print(request.headers) #only works for python
    return "Waaaa hooo HAAAH"

if __name__ == "__main__":
    app.debug = True
    app.run()
