import requests
import json
import sys
import os
import requests
from flask import Flask, request, abort
import utils
import tokens

app = Flask(__name__)


GITHUB_SECRET = tokens.github



bearer = tokens.webex
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer " + bearer
}


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def teams_webhook():
    if request.method == 'POST':
        webhook = request.get_json(silent=True)
        if request.headers['Content-Type'] == 'application/json':
            data = request.json
            utils.send_msg(data)
        return "true"
    elif request.method == 'GET':
        message = " bot is up and running.</b></h2></center>" 
        return message

 

if __name__ == "__main__":
    utils.main()

 
