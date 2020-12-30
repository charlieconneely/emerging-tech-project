## Emerging Technologies 20/21 - Project
### Charlie Conneely - G00348887
This repository contains an application which trains a neural network to predict the power output of a wind turbine 
based off an input wind speed value. <br/> The model was trained using the data within `powerproduction.txt` <br/><br/>
***
**Contents:** <br/>
* `model.ipynb` :
  * Jupyter Notebook file which trains the neural network and outlines it's accuracy.
* `server.py` :
  * Server which routes user to index.html. 
  * Loads the model trained in `model.ipynb`.
  * Handles requests from `index.html`.
* `static/index.html` :
  * User interface.

***
**Linux**
```bash
export FLASK_APP=server.py
python3 -m flask run
```

**Windows**
```bash
set FLASK_APP=server.py
python -m flask run
```
***
**Dependencies**
* Python v3.7.0
* Jupyter Notebook v5.6.0
* Anaconda v4.9.2
* Tensorflow v1.13.1
