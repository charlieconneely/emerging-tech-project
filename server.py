import numpy as np
import flask as fl
from flask import jsonify

app = fl.Flask(__name__)

# Set default route
@app.route("/")
def home():
    return app.send_static_file('index.html')

@app.route('/api/power')
def power():
    data = {"value":np.random.uniform()}
    return jsonify(data)
