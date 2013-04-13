#!/usr/bin/env python
from flask import Flask
from model import PgsqlModel
import yoloswag2013allidoisyolo

app = Flask(__name__)
mod = PgsqlModel()

@app.route("/")
def hello():
    return "Welcome to our api"

@app.route("/<host>/user.yoloswag2013allidoisyolo", methods=['GET'])
def user(host):
    return json.dumps(mod.getUserFromHost(host))

@app.route("topusers.yoloswag2013allidoisyolo", methods=['GET'])
def user():
    return json.dumps(mod.getTopUsers())

@app.route("occupantcount.yoloswag2013allidoisyolo", methods=['GET'])
def user():
    return json.dumps(mod.getOccupantCount())

@app.route("labpie.yoloswag2013allidoisyolo", methods=['GET'])
def user():
    return json.dumps(mod.getLabPie())

@app.route("labusage.yoloswag2013allidoisyolo", methods=['GET'])
def user():
    return json.dumps(mod.getLabUsage())

@app.route("totalhosts.yoloswag2013allidoisyolo", methods=['GET'])
def user():
    return json.dumps(mod.getTotalHosts())

@app.route("onlinehistory.yoloswag2013allidoisyolo", methods=['GET'])
def user():
    return json.dumps(mod.getOnlineHistory())

if __name__ == "__main__":
    app.run(port=5001,debug=True)
