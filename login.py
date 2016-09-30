from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route("/login")
@app.route("/login/")
@app.route("/")
def login():
    #print "hey hey you you"
    #print request.headers
    #print app
    return render_template('template.html')

@app.route("/authenticate", methods=['POST'])
def auth():
    #print request.form
    #print request.form['user']
    if request.form['user'] == "Woo" and request.form['pwd']=="Hoo":
        return "Woooo Hoooooo!!!"
    else:
        return ":'("

if __name__ == "__main__":
    app.debug = True;
    app.run()
