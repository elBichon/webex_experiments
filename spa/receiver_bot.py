import requests
import json
import sys
import os
import tokens
from flask import Flask, render_template, request, flash, session
try:
    from flask import Flask
    from flask import request
except ImportError as e:
    print(e)
    print("Looks like 'flask' library is missing.\n"
          "Type 'pip3 install flask' command to install the missing library.")
    sys.exit()

 

 

bearer = tokens.answer_bot

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer " + bearer
}



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
    return "Sure! I can help. Below are the commands that I understand:<br/>" \
           "`Help me` - I will display what I can do.<br/>" \
           "" \

def greetings():
    return "Hi my name is %s.<br/>" \
           "Type `Help me` to see what I can do.<br/>" % bot_name

 

app = Flask(__name__)
@app.route('/', methods=['POST'])
def teams_webhook():
    webhook = request.get_json(silent=True)
    result = send_get('https://api.ciscospark.com/v1/messages/{0}'.format(webhook['data']['id']))
    in_message = result.get('text', '').lower()
    in_message = in_message.replace(bot_name.lower() + " ", '')
    if in_message.startswith('help me'):
        msg = help_me()
        print(msg)
        request1 = requests.post('https://webexapis.com/v1/messages', json.dumps({"toPersonEmail": "sender_bot1@webex.bot","text": msg}), headers=headers).json()
    elif in_message.startswith('hello'):
        msg = greetings()
        print(msg)
        request1 = requests.post('https://webexapis.com/v1/messages', json.dumps({"toPersonEmail": "sender_bot1@webex.bot","text": msg}), headers=headers).json()
    return 'True'

 
def main():
    global bot_email, bot_name
    if len(bearer) != 0:
        test_auth = send_get("https://api.ciscospark.com/v1/people/me", js=False)
        if test_auth.status_code == 401:
            print("Looks like the provided access token is not correct.\n"
                  "Please review it and make sure it belongs to your bot account.\n"
                  "Do not worry if you have lost the access token. "
                  "You can always go to https://developer.webex.com/my-apps "
                  "and generate a new access token.")
            sys.exit()
        if test_auth.status_code == 200:
            test_auth = test_auth.json()
            bot_name = test_auth.get("displayName","")
            bot_email = test_auth.get("emails","")[0]
    else:
        print("'bearer' variable is empty! \n"
              "Please populate it with bot's access token and run the script again.\n"
              "Do not worry if you have lost the access token. "
              "You can always go to https://developer.webex.com/my-apps "
              "and generate a new access token.")
        sys.exit()
    if "@webex.bot" not in bot_email:
        print("You have provided an access token which does not relate to a Bot Account.\n"
              "Please change for a Bot Account access token, view it and make sure it belongs to your bot account.\n"
              "Do not worry if you have lost the access token. "
              "You can always go to https://developer.webex.com/my-apps "
              "and generate a new access token for your Bot.")
        sys.exit()
    else:
        app.debug = True
        app.run(host='localhost', port=8080)

if __name__ == "__main__":
    main()