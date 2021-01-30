from flask import Flask, render_template, request, flash, session

app = Flask(__name__)

answer = ""

@app.route("/msg", methods=["POST", "GET"]) 
def upvote():
	try:
		if len(str(request.form["search"])) > 0 and isinstance(request.form["search"],str) == True:
			answer = str(request.form["search"]) + "aaaa1"
		else:
			answer = "invalid input"
			return answer
		return str(answer)
	except:
		answer = "invalid input"
		return answer


@app.route("/")
def index():
	return render_template("index.html")

