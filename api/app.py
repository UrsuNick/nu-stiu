from flask import Flask, render_template, request, session, redirect
from supabase import create_client, Client

app = Flask(__name__)
app.secret_key = "0"

url = "https://oyhqtmhndpaehtcwisgp.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im95aHF0bWhuZHBhZWh0Y3dpc2dwIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxODg5ODE3MywiZXhwIjoyMDM0NDc0MTczfQ.YL2P3KIJCYzRpsZW5Vzz1ihOqlB6VdjRrNkOBynqXE8"
supabase: Client = create_client(url, key)


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("username", False):
        return redirect("/home")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        data = supabase.from_("users").select("*").eq("user_name", username).execute()
        if data.data != [] and data.data[0]["password"] == password:
            session["username"] = True
            return redirect("/home")
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        data = supabase.from_("users").select("*").eq("user_name", username).execute()

        if data.data == []:

            data, count = (
                supabase.table("users")
                .insert({"user_name": username, "password": password})
                .execute()
            )
            return redirect("/login")
    return render_template("register.html")


@app.route("/home")
def home():
    if session.get("username", False):
        return render_template("home.html")
    return redirect("/login")


@app.route("/log-out", methods=["POST"])
def log_out():
    session.clear()
    return redirect("/login")


def test():
    data = supabase.from_("users").select("user_name, password").execute()
    print(data)


test()
