import sys
import os
import json
import requests
from flask import Flask, request, abort
import tokens 
GITHUB_SECRET = tokens.github
bearer = tokens.webex
roomId = tokens.roomId
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer " + bearer
}

#utils library

def send_get(url, payload=None,js=True):
    if payload == None:
        request = requests.get(url, headers=headers)
    else:
        request = requests.get(url, headers=headers, params=payload)
    if js == True:
        request= request.json()
    return request

def send_post(url, data):
    request = requests.post(url, json.dumps(data), headers=headers).json()
    return request

def help_me():
    return "Hello! Sure! I can help. Below are the commands that I understand: `Help me` - I will display what I can do. My job is to send you and the rest of your team notifications when something happens inside your repository on pull or push events" 

def greetings():
    return "Hi, type `Help me` to see what I can do.<br/>" 
 


def send_msg(data):
    if str(data['action']) == 'opened':
        msg = 'the user ' +str(data['pull_request']['user']['login'])+' opened a pull request at url: '+str(data['pull_request']['url'])
        send_post("https://api.ciscospark.com/v1/messages", {"roomId": roomId,"markdown": msg})
    elif str(data['action']) == 'unlabeled':
        msg = 'the user ' +str(data['pull_request']['user']['login'])+' made a request to unlabel at url: '+str(data['pull_request']['url'])
        send_post("https://api.ciscospark.com/v1/messages", {"roomId": roomId,"markdown": msg})
    elif str(data['action']) == 'labeled':
        msg = 'the user ' +str(data['pull_request']['user']['login'])+' made a request to label at url: '+str(data['pull_request']['url'])
        send_post("https://api.ciscospark.com/v1/messages", {"roomId": roomId,"markdown": msg})
    elif str(data['action']) == 'closed':
        msg = 'the user ' +str(data['pull_request']['user']['login'])+' closed a pull request at url: '+str(data['pull_request']['url'])
        send_post("https://api.ciscospark.com/v1/messages", {"roomId": roomId,"markdown": msg})
    else:
        msg = 'the user ' +str(data['pull_request']['user']['login'])+' made a request at url: '+str(data['pull_request']['url'])
        send_post("https://api.ciscospark.com/v1/messages", {"roomId": roomId,"markdown": msg})
