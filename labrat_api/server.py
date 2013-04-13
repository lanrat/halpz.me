#!/usr/bin/env python
from flask import Flask
from model import PgsqlModel
import json

app = Flask(__name__)
mod = PgsqlModel()

@app.route("/")
def hello():
    return "Welcome to our api"

@app.route("/location.json", methods=['GET'])
def location():
    return json.dump(getLocationFromHost(request.form['host']))

@app.route("/user.json", methods=['GET'])
def user():
    return json.dump(getUserFromHost(request.form['host']))

if __name__ == "__main__":
    app.run()
