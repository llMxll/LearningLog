from flask import Flask, request, redirect, session
from replit import db
import os

app = Flask(__name__)
app.secret_key = os.environ["sessionKey"]

@app.route('/logOut', methods=["POST"])
def logOut():
  session.clear()
  return redirect("/")


@app.route('/login', methods=["POST"])
def login():
    user = request.form
    username = user["username"].lower()
    try:
        if user["username"].lower() in db:
            if user["password"] == db[username]["password"]:
              session["username"] = username
              return redirect("/welcome")
            else:
                return "Username or password incorrect"
        else:
            return "Username or password incorrect"
    except:
        return "error"

@app.route('/adduser', methods=["POST"])
def adduser():
    user = request.form
    if user["username"].lower() in db:
        return "Username not available"
    else:
        db[user["username"].lower()] = {
            "name": user["name"],
            "password": user["password"]
        }
        return redirect("/register")

@app.route('/welcome')
def welcome():
    if session.get("username"):
      page = ""
    
      f = open("welcome.html", "r")
      page = f.read()
      f.close() 
  
      if session.get("username"):
        name = session["username"]      
        page = page.replace("{name}", name)
  
      return page
    else:
      return redirect("/")  

@app.route('/register', methods=["GET"])
def register():
    if session.get("username"):
      return redirect("/welcome")
    page = ""

    f = open("register.html", "r")
    page = f.read()
    f.close()

    try:
        get = request.args
        if get["state"] == "register":
            page = page.replace("{button}",
                                '<button value="submit">Submit</button>')
            page = page.replace("{action}", '/adduser')
            page = page.replace(
                "{name}",
                '<p>Name: <input type="text" name="name" required></p>')
    except:
        page = page.replace("{button}",
                            '<button value="submit">Log in</button>')
        page = page.replace("{action}", '/login')
        page = page.replace("{name}", "")

    return page


@app.route('/')
def index():
    if session.get("username"):
      return redirect("/welcome")
  
    page = ""

    f = open("index.html", "r")
    page = f.read()
    f.close()

    return page


app.run(host="0.0.0.0", port=81)
