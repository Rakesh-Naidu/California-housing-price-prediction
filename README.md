# California-housing-price-prediction 🏠🏘✔

## Table of Contents
  * [Demo](#demo)
  * [Overview](#overview)
  * [About the dataset](#about-the-dataset)
  * [Dataset description](#dataset-description)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [Technologies used](#technologies-used)

## Demo
Link: [https://housingpricepred-api.herokuapp.com/](https://housingpricepred-api.herokuapp.com/)

[![](https://user-images.githubusercontent.com/44801151/106480054-fb7a3f00-64d0-11eb-8f5a-af3295b65dbd.png)](https://housingpricepred-api.herokuapp.com/)

[![](https://user-images.githubusercontent.com/44801151/106480252-2f556480-64d1-11eb-8220-6145286b7603.png)](https://housingpricepred-api.herokuapp.com/)

## Overview
This is a Flask web app which predicts the median value of house.

## About the dataset
Link: [https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.tgz](https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.tgz)

Information is collected on the variables using all the block groups in California from the 1990 Census. In this sample a block group on average includes 1425.5 individuals living in a geographically compact area. Naturally, the geographical area included varies inversely with the population density. Distances are computed among the centroids of each block group as measured in latitude and longitude. All the block groups reporting zero entries for the independent and dependent variables are excluded. The final data contained 20,640 observations on 9 characteristics.

# Dataset description
Column title |	Description	| Range	| Datatype
--- | ----- | ---------- | ---
longitude	| A measure of how far west a house is; a higher value is farther west	| <ul> <li>Longitude values range from -180 to +180</li>  <li>Data set min: -124.3</li> <li>Data set max: -114.3</li> </ul> | float64
latitude	| A measure of how far north a house is; a higher value is farther north	| <ul> <li>Latitude values range from -90 to +90</li> <li>Data set min: 32.5</li> <li>Data set max: 42.5</li> </ul>| float64
housingMedianAge	| Median age of a house within a block; a lower number is a newer building	| <ul> <li>Data set min: 1.0</li> <li>Data set max: 52.0</li> </ul> | float64
totalRooms	| Total number of rooms within a block	| <ul> <li>Data set min: 2.0</li> <li>Data set max: 37937.0</li> </ul>| float64
totalBedrooms	| Total number of bedrooms within a block	 | <ul> <li>Data set min: 1.0</li> <li>Data set max: 6445.0</li> </ul> | float64
population |	Total number of people residing within a block	| <ul> <li>Data set min: 3.0</li>  <li>Data set max: 35682.0</li> </ul> | float64
households	| Total number of households, a group of people residing within a home unit, for a block	| <ul> <li>Data set min: 1.0</li> <li>Data set max: 6082.0</li> </ul> | float64
medianIncome | Median income for households within a block of houses (measured in tens of thousands of US Dollars)	 | <ul>  <li>Data set min: 0.5</li> <li>Data set max: 15.0</li> </ul> | float64
medianHouseValue	| Median house value for households within a block (measured in US Dollars)	| <ul> <li>Data set min: 14999.0</li> <li>Data set max: 500001.0</li> </ul> | float64

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
