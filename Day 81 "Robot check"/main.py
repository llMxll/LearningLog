from flask import Flask, request

app = Flask(__name__)

@app.route('/detectAI', methods=["POST"])
def detectAI():
  form = request.form
  acceptResponse = True
  
  if form["test1"] != "no":
    acceptResponse = False
  if form["test2"].lower() == "error":
    acceptResponse = False
  if form["test3"] != "humanFood":
    acceptResponse = False
  if acceptResponse == True:
    page = "Welcome fellow human"
  else:
    page = "10101110110111101"

  return page
    

@app.route('/')
def index():
  page = ""
  f = open("index.html", "r")
  page = f.read()
  f.close()

  return page

app.run(host = "0.0.0.0", port = "81")

