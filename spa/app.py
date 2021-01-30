from flask import Flask, render_template, request, flash, session

app = Flask(__name__)

answer = ""

@app.route("/msg", methods=["POST", "GET"]) 
def upvote():
	answer = str(request.form["search"]) + "aaaa1"
	return str(answer)

@app.route("/")
def index():
	return render_template("index.html")

