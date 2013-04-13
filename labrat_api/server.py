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
def topusers():
    return json.dumps(mod.getTopUsers())

@app.route("occupantcount.json", methods=['GET'])
def occupantcount():
    return json.dumps(mod.getOccupantCount())

@app.route("labpie.json", methods=['GET'])
def labpie():
    return json.dumps(mod.getLabPie())

@app.route("labusage.json", methods=['GET'])
def labusage():
    return json.dumps(mod.getLabUsage())

@app.route("totalhosts.json", methods=['GET'])
def totalhosts():
    return json.dumps(mod.getTotalHosts())

@app.route("onlinehistory.json", methods=['GET'])
def onlinehistory():
    return json.dumps(mod.getOnlineHistory())

if __name__ == "__main__":
    app.run(port=5001,debug=True)
