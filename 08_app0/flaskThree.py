from flask import Flask
app = Flask(__name__)

@app.route("/") #assign following function to run when root route requested
def hello_world():
    print(__name__) #where will this go?
    return "No hablo queso!"

@app.route("/two") #url
def world2():
    print(__name__)
    return "Second route? I sure hope it is."

@app.route("/three") #url
def world3():
    print(__name__)
    return "It's the third parallel universe! How do I get back?"

if __name__ == "__main__":
    app.debug = True
    app.run()
