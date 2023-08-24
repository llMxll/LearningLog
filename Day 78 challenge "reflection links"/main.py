from flask import Flask

app = Flask(__name__)
entry = {}

entry["78"] = {"content": "The day I made this link page"}

@app.route('/')
def index():
    content = ""
    for i in range(78, 101):
        content += f'<a href="/{i}">Replit Day {i}</a><br>'

    f = open("templates/index.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{content}", content)

    return page


@app.route('/<pageNumber>')
def main(pageNumber):
    dayNumber = str(pageNumber)

    f = open("templates/main.html", "r")
    page = f.read()
    f.close()
    try:
        content = entry[str(pageNumber)]["content"]
    except:
        content = ""

    page = page.replace("{dayNumber}", dayNumber)
    page = page.replace("{content}", content)
    return page


app.run(host='0.0.0.0', port=81)
