import sys
import os
import json
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
            data = request.json#json.dumps(request.json)
            utils.send_msg(data)   
        return "true"
    elif request.method == 'GET':
        message = " bot is up and running.</b></h2></center>" 
        return message

def main():
    global bot_email, bot_name
    if len(bearer) != 0:
        test_auth = utils.send_get("https://api.ciscospark.com/v1/people/me", js=False)
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

 
