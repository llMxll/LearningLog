from flask import Flask, redirect, request, session
from replit import db
import os, datetime

app = Flask(__name__)
app.secret_key = os.environ["sessionKey"]

username = "mx"
password = "pass"


@app.route('/add_entry', methods=["POST"])
def addEntry():
    get = request.form
    db[f"entry{datetime.datetime.now()}"] = get

    return redirect('/')


@app.route('/logout', methods=["POST"])
def logout():
    session.clear()
    return redirect('/')


@app.route('/verify', methods=["POST",])
def verify():
    get = request.form
    if get["username"] == username:
        if get["password"] == password:
            session["username"] = get["username"]
            return redirect('/')
        else:  
          return redirect('/login')
    else:  
        return redirect('/login')


@app.route('/login', methods=["POST", "GET"])
def login():

    f = open("login.html", "r")
    page = f.read()
    f.close()

    return page


@app.route('/', methods=["GET"])
def index():
    if session.get("username"):
        logged_in = True
    else:
        logged_in = False

    f = open("index.html", "r")
    page = f.read()
    f.close()

    if logged_in == False:
        page = page.replace('{login_logout_button}', 'login')
        page = page.replace('{login_logout_function}', '/login')
        page = page.replace('{entry_creation_form}', '')
    else:
        page = page.replace('{login_logout_button}', 'logout')
        page = page.replace('{login_logout_function}', '/logout')
        page = page.replace(
            '{entry_creation_form}',
            """<p>Title: <input type="text", name="title"></p>
      <p>Date: <input type="date", name="date"></p>
      <p>Body text: <input type=text, name=entry></p>
            
      <button value=submit>save</button>
      """)

    content = ""
    for i in db:
        content = f"""<h3>{db[i]["title"]}</h3>
      <h4>{db[i]["date"]}</h4>
      <p>{db[i]["entry"]}</p>
      """ + content

    page = page.replace('{content}', content)

    return page


app.run(host='0.0.0.0', port=81)
