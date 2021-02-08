# importing the requests library 

import json
import requests
from flask import Flask, request, abort
import tokens 

bearer = tokens.webex
roomId = tokens.roomId
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer " + bearer
}

def send_post(url, data, headers):
    request = requests.post(url, json.dumps(data), headers=headers).json()
    return request
msg = 'sendfing from my script'
send_post("https://api.ciscospark.com/v1/messages", {"roomId": roomId,"markdown": msg}, headers)

