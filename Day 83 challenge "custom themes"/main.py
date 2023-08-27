from flask import Flask, request

app = Flask(__name__, static_url_path="/static")


@app.route('/', methods=["GET"])
def index():
    style = "style"
    get = request.args
    if get != {}:
        style = get["style"]

    title = "Home"
    date = ""
    text = """<a href =/entry1>Entry 1</a><br>
<a href =/entry2>Entry 2</a>
  """

    page = ""
    f = open("templates/temp.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{title}", title)
    page = page.replace("{date}", date)
    page = page.replace("{text}", text)
    page = page.replace("{style}", style)

    return page


@app.route('/entry1', methods=["GET"])
def entry1():
    style = "style"
    get = request.args
    if get != {}:
        style = get["style"]

    title = "First entry"
    date = "23rd August 2023"
    text = """This is the first entry
  <br>
  <a href =/>Home</a>"""
    page = ""
    f = open("templates/temp.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{title}", title)
    page = page.replace("{date}", date)
    page = page.replace("{text}", text)
    page = page.replace("{style}", style)
  
    return page


@app.route('/entry2', methods=["GET"])
def entry2():
    style = "style"
    get = request.args
    if get != {}:
        style = get["style"]

    title = "Second entry"
    date = "23rd August 2023"
    text = """This is the Second entry
  <br>
  <a href =/>Home</a>"""
    page = ""
    f = open("templates/temp.html", "r")
    page = f.read()
    f.close()
  
    page = page.replace("{title}", title)
    page = page.replace("{date}", date)
    page = page.replace("{text}", text)
    page = page.replace("{style}", style)
    return page


app.run(host='0.0.0.0', port=81)
