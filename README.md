# Aircraft Accidents Analytics
![Python](https://img.shields.io/badge/python-%23F0F0F0?style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAACXBIWXMAAAsTAAALEwEAmpwYAAADGUlEQVR4nO2YPWgUQRTHZ2dzM5dYaCFBAiaFNkZRBMUuiI0fRdBCwSZFolj4kWCSmRMJhyksBJVgI2qhhYIpFEREczPZmUSDSBo%2FkIAERWMnETQmSDRPdm89g4TczCXrXnD%2F8Jpr9vfb92Z25hBKkiRJEoTAQTy3GWcEd7i8i7l4hZkYx0x%2Bx1xMYi4%2BYCaeOlxecrncgbJZXD5vrUNsDIC5BNNyuHiITnor40ZHKHuvCjM5ZgNfKCaHYu%2BEy%2Fp3lgQflpvJ7YpVAHPZHL7NMXRK1COeq8VcvrAYpe54BZhoy4PIa39%2Bk13mAvJiWQgUOtAu6%2Bw6IMtEoMRyEoGYu%2BSEHQBN2kBTmFVToOkzUGTfUhWAoBSdAU0Plf70jLfW4fJy%2BKWdWMi8lySgg%2FoKMl1nze52ykbM5LfFhi5BAEDRs3b0%2Be1w0d%2F4HALnzQTIqBW%2Fw0VP1PBBMXEsEFDk9LwCfnlVq4wFMBNvohcQn1H7o%2Bp8B%2BjtogKK7DGjb%2FVWYC5mIhaY8A%2BCyId%2Fsqw6WKjFBVrNBHhuezTjIn9iJt87TF5FHXLN78eBpreKwufrjNn4ZORBy1EYwVw2oc6%2BmuBmZhgAhEHRC4bw%2Fk50zkyAi6Pmu4i4iY4%2FoKbQhZFRqQOg6LAxfH6EuJkAEy2GW2A%2FynoVAdTjyhrQtAc0eQua%2FrAC06YC6SYjAbdT7DWZZ8T61gXwXsUW0ORTJNB6Vg2mNpn1mMn1BgJDeXiUBk3eRQ6v6CQMo5SZwP5et9hX2OHiSiCgSGPk8DqoO8gmDhPS6AyjyIl%2FAD%2Ftj6mVAGbiiJFAsTPMYsAr2oysw3PL5%2Fu%2FJ2KBKdD0NShy3XzhzhGXid2YiemSBRSN98IehMsGf7%2F%2F%2B16wdASKZMEjpGKW%2FM8EyBgMkHrQ6dWg6POlJ6BI4e9H0KSrTARoi4XAR%2FBSG2AwXQuavgwFuuMVCEZiAWvAo4djFTC%2Bz869gL9YXdQjExhGVaDJDTt4Mgo63YDKKaAqtvrXPlBEh0fsifAsMw6KjoCi90GRLAxUboNe5MbNmyRJElQe%2BQWgfIcmva%2Bj%2BwAAAABJRU5ErkJggg%3D%3D)
![Flask](https://img.shields.io/badge/flask-black?style=for-the-badge&logo=flask)
![SQLite](https://img.shields.io/badge/sqlite-%23003B57?style=for-the-badge&logo=sqlite)
![Bootstrap5](https://img.shields.io/badge/bootstrap-%237952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

## Table of Contents
 - [About](#about)
 - [Project Setup](#project-setup)
 - [Dependencies](#dependencies)
 - [Execution](#execution)

## About
A web application to display and analyze aircraft disaster data, regarding the history of airplane crashes throughout the world, from 1928 to 2019. This includes flights made by commercial passenger airlines, cargo freights, military and private flights, from assorted countries.

In Python, made using Flask, SQLite and Bootstrap5, and it uses data from a Kaggle dataset.

## Project Setup

### Directories structure
 - **/ :** root directory of the project.
 - **/sql :** SQL code files for creating and populating data structures.
 - **/static :** all static assets, such as Javascript and CSS files.
 - **/templates :** templates for the views using mainly HTML and Jinja.

### Techstack
 Made in Python, it uses Flask microframework as the web server gateway interface (WSGI), with SQLite database. It uses Jinja, HTML, JavaScript, and is styled with CSS (Bootstrap 5). For more details, see [Dependencies](#dependencies).
 
 - Python (3.9.18)
 - Flask
 - SQLite
 - Bootstrap

## Dependencies
### Getting Started with Flask
Web framework used was [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/#install-flask) (3.0.2). Application uses [Jinja](https://jinja.palletsprojects.com/en/3.1.x/intro/#installation) (3.1.3) templating.

### Getting Started with Bootstrap
Styled with [Bootstrap 5](https://getbootstrap.com/docs/5.2/getting-started/download/).

## Execution
- `export FLASK_APP=app.py`
- `flask run --port 5001`, to run on a different port, change the port number.
