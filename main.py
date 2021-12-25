import flask
import os
app = flask.Flask(__name__, static_url_path='/static', static_folder='static')

PORT = 3000


@app.route('/', methods=['GET', 'POST'])
def index():
    return flask.render_template('index.html')



app.run(port=PORT)