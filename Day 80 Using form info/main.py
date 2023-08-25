from flask import Flask, request

app = Flask(__name__)
logins = {}
logins["mx"] = {"password": "111"}
logins["yhu"] = {"password": "222"}
logins["anon"] = {"password": "333"}


@app.route('/userLogin', methods=["POST"])
def userLogin():
    page = ""
    form = request.form

    if form["username"] in logins.keys():
        if form["password"] == logins[form["username"]]["password"]:
            page = "Login successful"
        else:
            page = "Get outta here hackzor"
    else:
        page = "User not found"

    return page


@app.route('/')
def index():
    page = ""

    f = open("index.html", "r")
    page = f.read()
    f.close()

    return page


app.run(host='0.0.0.0', port=81)
