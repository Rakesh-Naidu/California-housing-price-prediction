# Housting-price-prediction:

## Table of Contents
  * [Demo](#demo)
  * [Overview](#overview)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [Technologies used](#technologies-used)

## Demo
Link: [https://housingpricepred-api.herokuapp.com/](https://housingpricepred-api.herokuapp.com/)

[![](https://user-images.githubusercontent.com/44801151/106467590-e1d1fb00-64c2-11eb-965a-3ed9d878d3ac.png)](https://housingpricepred-api.herokuapp.com/)

[![](https://user-images.githubusercontent.com/44801151/106467837-32e1ef00-64c3-11eb-8732-96ba1b927161.png)](https://housingpricepred-api.herokuapp.com/)

## Overview
This is a Flask web app which predicts the median value of house.

## Installation
The Code is written in Python 3.6.10. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Deployement on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Directory Tree 
```
├── static 
│   ├── css
|   |   ├── cssfile.css
|   |   ├── h3.jpg
├── template
│   ├── index.html
├── Procfile
├── README.md
├── app.py
├── Housing_Price_EDA.ipynb
├── Housing_Model.ipynb
├── model.pkl
├── housing.csv
├── requirements.txt
```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) 
