from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key="0"

@app.route("/")
def index():

    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("username",False):
        return redirect("/home")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "test" and password == "test":
            session["username"]=True
            return redirect("/home")    
    return render_template("login.html")


@app.route("/home")
def home():
    if session.get("username",False):
        return render_template("home.html")
    return redirect("/login")

@app.route("/log-out",methods=["POST"])
def log_out():
    session.clear()
    return redirect("/login")

