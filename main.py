import flask
import os
app = flask.Flask(__name__, static_url_path='/static', static_folder='static')

PORT = int(os.environ.get("PORT", 3000))


@app.route('/', methods=['GET', 'POST'])
def index():
    return flask.render_template('index.html')



app.run(host="0.0.0.0",port=PORT)