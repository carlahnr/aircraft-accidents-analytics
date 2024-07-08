# Aircraft Accidents Analytics
![Python](https://img.shields.io/badge/python-yellow?style=for-the-badge&logo=python&logoColor=%233776AB)
![Flask](https://img.shields.io/badge/flask-black?style=for-the-badge&logo=flask)
![SQLite](https://img.shields.io/badge/sqlite-%23003B57?style=for-the-badge&logo=sqlite)
![Bootstrap5](https://img.shields.io/badge/bootstrap-%237952B3?style=for-the-badge&logo=pandas&color=%237952B3)

## Table of Contents
 - [About](#about)
 - [Project Setup](#project-setup)
 - [Dependencies](#dependencies)
 - [Execution](#execution)

## About
A web application to display and analyze airplane crash data. In Python, it uses Flask, SQLite and Bootstrap5.

## Project Setup

### Directories structure
 - **/ :** root directory of the project.

### Endpoints
 The app contains 2 endpoints:
 - **Home view:** description of the app.
 - **Stats view:** main funcionality view.

### Techstack
 Made in Python, it uses Flask microframework as the web server gateway interface (WSGI). It uses Jinja, HTML, JavaScript, and is styled with CSS (Bootstrap 5). For more details, see [Dependencies](#dependencies).
 
 - Python (3.9.18)
 - Flask
 - Bootstrap

## Dependencies
### Getting Started with Flask
Web framework used was [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/#install-flask) (3.0.2). Application uses [Jinja](https://jinja.palletsprojects.com/en/3.1.x/intro/#installation) (3.1.3) templating.

### Getting Started with Bootstrap
Styled with [Bootstrap 5](https://getbootstrap.com/docs/5.2/getting-started/download/). Also uses [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/docs/) (1.6.0) and [Dash Bootstrap Templates](https://pypi.org/project/dash-bootstrap-templates/) (1.1.2).

## Execution
- `export FLASK_APP=app.py`
- `flask run --port 5001`, to run on a different port, change the port number.
