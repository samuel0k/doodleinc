import json
import flask
import os
import threading

from werkzeug.utils import redirect
app = flask.Flask(__name__, static_url_path='/static', static_folder='static')

PORT = int(os.environ.get("PORT", 3000))


@app.route('/', methods=['GET'])
def index():
    return flask.render_template('index.html')

@app.route('/adm', methods=["GET"])
def adm():

    return flask.render_template('adm.html')

@app.route('/login', methods=["POST"])
def login():
    username = flask.request.form.get("username")
    password = flask.request.form.get("password")

    if username == "e338f1eead033ff35ccb58d963d0a085" and password == "20c34b720593668505bc2529085b5863":
        print("Logged in!")
        return flask.redirect("/adm")
    else:
        print("Wrong credentials")
        return flask.redirect("/")




def build(domain, port):
    print("Building!")

    f = open("serv.json", "r")
    json_obj = json.load(f)
    f.close()
    json_obj["domain"] = domain
    json_obj["port"] = port

    d = open("serv.json", "w")
    json.dump(json_obj, d)
    d.close()

    os.system("pyinstaller --onefile --clean --distpath static/ dd.py")


@app.route('/admc', methods=["POST"])
def admc():
    domain = flask.request.form.get("domain")
    port = flask.request.form.get("port")

    if len(domain) > 0 and len(port) > 0:
        thr = threading.Thread(target=build, args=(domain, port))
        thr.start()
    return flask.redirect('/adm')

app.run(host="0.0.0.0",port=PORT)