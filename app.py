import dash
from flask import Flask, redirect
import logging
logging.basicConfig(format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s', level=logging.INFO)

from datetime import datetime as dt

# https://dash.plotly.com/layout
# https://plotly.com/python/plotly-express/

server = Flask(__name__)

@server.route('/')
def index():
	return redirect('/dashboard/')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',"./assets/common.css"]
app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets, url_base_pathname='/dashboard/')
#app.css.append_css({"external_url": ["./assets/common.css"]})
#app.scripts.config.serve_locally=True
app.config['suppress_callback_exceptions'] = True

