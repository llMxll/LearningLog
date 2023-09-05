import os, requests, json
from flask import Flask, request, redirect
from requests.auth import HTTPBasicAuth
from replit import db

app = Flask(__name__)
db['content'] = ""

@app.route("/search_api", methods=["POST"])
def search_api():
  year = request.form["year"]

  #Get ID and secret from website
  clientID = os.environ['CLIENT_ID']
  clientSecret = os.environ['CLIENT_SECRET']

  # Get access token
  url = "https://accounts.spotify.com/api/token"
  data = {"grant_type": "client_credentials"}
  auth = HTTPBasicAuth(clientID, clientSecret)
  response = requests.post(url, data=data, auth=auth)
  accessToken = response.json()["access_token"]

  #Search parameters -- mostly copied from website
  url = "https://api.spotify.com/v1/search"
  headers = {'Authorization': f'Bearer {accessToken}'}

  offset = db['offset']
  search = f"?q=year%3A{year}&type=track&limit=10&offset={offset}"
  
  db['offset'] += 10
  if db['offset'] > 200:
    db['offset'] = 0

  fullURL = f"{url}{search}"

  #Search
  response = requests.get(fullURL, headers=headers)
  data = response.json()

  db['content'] = ""
  for track in data["tracks"]["items"]:

    db['content'] += f"""{track["name"]}:<br>
    <audio controls>
    <source src="{track["preview_url"]}" type="audio/mpeg">
    </audio><br><hr>"""
  print(db['content'])
  
  return redirect("/")


@app.route("/")
def index():
  f = open("index.html")
  page = f.read()
  f.close()

  page = page.replace("{content}", db['content'])

  return page


app.run(host="0.0.0.0", port=81)
