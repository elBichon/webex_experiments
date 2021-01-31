import os
import json
import requests
from flask import Flask, request, abort

app = Flask(__name__)


GITHUB_SECRET = "dbdb459a70a7ec73bcb2707d71593f5acf1fe091"


@app.route("/payload", methods=['POST'])
def github_webhook_endpoint():
	if request.headers['Content-Type'] == 'application/json':
		data = json.dumps(request.json)
		print(data)
		return(data)


if __name__ == "__main__":
	app.run(debug=True)

