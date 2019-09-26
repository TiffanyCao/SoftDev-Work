#Tiffany Cao & Yaru Luo
#SoftDev1 pd1
#K12: Echo Echo Echo
#2019-09-26

from flask import Flask, render_template, request
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     print("hello")
#     return "hello world"

@app.route("/") #route for landing page
def test_tmplt():
    print(app)
    return render_template('form.html')


@app.route("/auth") #route for response page
def authenticate():
    #for testing
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
    return render_template('response.html',
        name = request.args['username']) #requests for the username given by user

# @app.route("/auth")
# def authenticate():
#     print(app)
#     print(request)
#     print(request.args)
#     print(request.args['username'])
#     print(request.headers)
#     return render_template('response.html',
#         name = request.args['username'])

if __name__ == "__main__":
    app.debug = True
    app.run()
