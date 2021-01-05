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

### Running the application with Docker

```bash
docker build . -t windpower-app
docker run --name windpower-container -d -p 5000:5000 windpower-app
```
After executing these commands, the application should be running on `127.0.0.1:5000` <br>
To kill and/or remove the container run:
```bash
docker kill <containerID>
docker rm <containerID>
```
The container ID can be observed by running:
```bash
docker container ls
``` 
***
### Running the application without Docker
**Linux**
```bash
export FLASK_APP=server.py
python3 -m flask run
```
***

**Windows**
```bash
set FLASK_APP=server.py
python -m flask run
```
***
**Dependencies used in development**
* Python v3.7.0
* Jupyter Notebook v5.6.0
* Anaconda v4.9.2
* Tensorflow v1.13.1
