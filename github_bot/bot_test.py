import requests
import json
import sys
import os
try:
    from flask import Flask
    from flask import request
except ImportError as e:
    print(e)
    print("Looks like 'flask' library is missing.\n"
          "Type 'pip3 install flask' command to install the missing library.")
    sys.exit()

 

import os
import json
import requests
from flask import Flask, request, abort

app = Flask(__name__)


GITHUB_SECRET = "dbdb459a70a7ec73bcb2707d71593f5acf1fe091"



bearer = "MWJjM2QzYzgtZWViNy00Y2NhLTg1M2QtN2UxN2NhMWZkYTNhNGQ5Zjk5NDMtMTA4_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
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
    print(str(request))
    return request

def help_me():
    return "Hello! Sure! I can help. Below are the commands that I understand: `Help me` - I will display what I can do. My job is to send you and the rest of your team notifications when something happens inside your repository on pull or push events" 

def greetings():
    return "Hi, type `Help me` to see what I can do.<br/>" 
 





app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def teams_webhook():
    if request.method == 'POST':
        webhook = request.get_json(silent=True)

        if request.headers['Content-Type'] == 'application/json':
            data = request.json#json.dumps(request.json)
            print(data)
#'actions' 'unlabelled', 'close' 'opened'
            if str(data['action']) == 'opened':
                msg = 'the user ' +str(data['pull_request']['user']['login'])+' opened a pull request at url: '+str(data['pull_request']['url'])
                send_post("https://api.ciscospark.com/v1/messages", {"roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vMTBlYTU1YjAtNWUzMi0xMWVhLWJjNjAtMDM2MzJiMTVmMWY4","markdown": msg})
            elif str(data['action']) == 'unlabeled':
                msg = 'the user ' +str(data['pull_request']['user']['login'])+' made a request to unlabel at url: '+str(data['pull_request']['url'])
                send_post("https://api.ciscospark.com/v1/messages", {"roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vMTBlYTU1YjAtNWUzMi0xMWVhLWJjNjAtMDM2MzJiMTVmMWY4","markdown": msg})
            elif str(data['action']) == 'labeled':
                msg = 'the user ' +str(data['pull_request']['user']['login'])+' made a request to label at url: '+str(data['pull_request']['url'])
                send_post("https://api.ciscospark.com/v1/messages", {"roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vMTBlYTU1YjAtNWUzMi0xMWVhLWJjNjAtMDM2MzJiMTVmMWY4","markdown": msg})
            elif str(data['action']) == 'closed':
                msg = 'the user ' +str(data['pull_request']['user']['login'])+' closed a pull request at url: '+str(data['pull_request']['url'])
                send_post("https://api.ciscospark.com/v1/messages", {"roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vMTBlYTU1YjAtNWUzMi0xMWVhLWJjNjAtMDM2MzJiMTVmMWY4","markdown": msg})
            else:
                msg = 'the user ' +str(data['pull_request']['user']['login'])+' made a request at url: '+str(data['pull_request']['url'])
                send_post("https://api.ciscospark.com/v1/messages", {"roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vMTBlYTU1YjAtNWUzMi0xMWVhLWJjNjAtMDM2MzJiMTVmMWY4","markdown": msg})
        return "true"
    elif request.method == 'GET':
        message = " bot is up and running.</b></h2></center>" 
        return message

 

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
        app.run(host='localhost', port=8080)
 

if __name__ == "__main__":
    main()

 
