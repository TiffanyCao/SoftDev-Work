# Amanda Zheng, Tiffany Cao, Yifan Wang -- Team Icky Toothpaste
# SoftDev2 pd1
# K18 -- Come Up For Air
# 2020-04-21

from flask import Flask, request, render_template

app = Flask(__name__)
ca=[]
ch=[]
fr=[]
ge=[]
ir=[]
it=[]
sk=[]
sp=[]
uk=[]
us=[]

f=open("static/countries.csv","r")
for line in f:
    if "Canada" in line:
        if(len(ca)<78):
            entry=line.strip("\n").split(",")
            ca.append(int(entry[4]))
    elif "China" in line:
        if(len(ch)<78):
            entry=line.strip("\n").split(",")
            ch.append(int(entry[4]))
    elif "France" in line:
        if(len(fr)<78):
            entry=line.strip("\n").split(",")
            fr.append(int(entry[4]))
    elif "Germany" in line:
        if(len(ge)<78):
            entry=line.strip("\n").split(",")
            ge.append(int(entry[4]))
    elif "Iran" in line:
        if(len(ir)<78):
            entry=line.strip("\n").split(",")
            ir.append(int(entry[4]))
    elif "Italy" in line:
        if(len(it)<78):
            entry=line.strip("\n").split(",")
            it.append(int(entry[4]))
    elif "South_Korea" in line:
        if(len(sk)<78):
            entry=line.strip("\n").split(",")
            sk.append(int(entry[4]))
    elif "Spain" in line:
        if(len(sp)<78):
            entry=line.strip("\n").split(",")
            sp.append(int(entry[4]))
    elif "United_Kingdom" in line:
        if(len(uk)<78):
            entry=line.strip("\n").split(",")
            uk.append(int(entry[4]))
    elif "United_States_of_America" in line:
        if(len(us)<78):
            entry=line.strip("\n").split(",")
            us.append(int(entry[4]))

ca=ca[::-1]
ch=ch[::-1]
fr=fr[::-1]
ge=ge[::-1]
ir=ir[::-1]
it=it[::-1]
sk=sk[::-1]
sp=sp[::-1]
uk=uk[::-1]
us=us[::-1]
@app.route("/")
def root():
    return render_template("index.html",canada=ca, china=ca, france=fr, germany =ge, iran = ir, italy=it, korea = sk, spain =sp, uk=uk, us=us)

if __name__ == "__main__":
    app.debug = True
    app.run()
