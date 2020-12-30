import numpy as np
import flask as fl
import tensorflow.keras as kr
from flask import jsonify

app = fl.Flask(__name__)

# Set default route
@app.route("/")
def home():
    return app.send_static_file('index.html')

@app.route("/api/power")
def power():
    loaded_model = kr.models.load_model('model.h5')
    result = loaded_model.predict([10.0])
    resultJSON = jsonify({"value":result.item(0)})
    #data = {"value":np.random.uniform()}
    return resultJSON
