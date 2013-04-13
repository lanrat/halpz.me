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

@app.route("topusers.json", methods=['GET'])
def user():
    return json.dumps(mod.getTopUsers())

@app.route("occupantcount.json", methods=['GET'])
def user():
    return json.dumps(mod.getOccupantCount())

@app.route("labpie.json", methods=['GET'])
def user():
    return json.dumps(mod.getLabPie())

@app.route("labusage.json", methods=['GET'])
def user():
    return json.dumps(mod.getLabUsage())

@app.route("totalhosts.json", methods=['GET'])
def user():
    return json.dumps(mod.getTotalHosts())

@app.route("onlinehistory.json", methods=['GET'])
def user():
    return json.dumps(mod.getOnlineHistory())

if __name__ == "__main__":
    app.run()
