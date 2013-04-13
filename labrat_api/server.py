#!/usr/bin/env python
from flask import Flask
from model import PgsqlModel
import json

app = Flask(__name__)
mod = PgsqlModel()

@app.route("/")
def hello():
    return "Welcome to our api"

@app.route("/<host>/user.json", methods=['GET'])
def user(host):
    return json.dumps(mod.getUserFromHost(host))

if __name__ == "__main__":
    app.run()
