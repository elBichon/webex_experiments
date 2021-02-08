from flask import Flask, render_template, request, flash, session
import re
import spacy
import flask
from nltk.tokenize import word_tokenize
import nltk
import pandas as pd
from gensim.parsing.preprocessing import remove_stopwords
import gensim
from gensim.models import Word2Vec
import nltk
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import utils 
import tokens
import requests
import json
import requests
from flask import Flask, request, abort
import tokens 
import time

bearer_sender = tokens.sender_bot
headers_post = {
    "Accept": "application/json",
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer " + bearer_sender
}

bearer_get = tokens.answer_bot
headers_get = {
    "Accept": "application/json",
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer " + bearer_get
}



def send_post(url, data, headers):
    request = requests.post(url, json.dumps(data), headers=headers).json()
    return request



app = Flask(__name__)

answer = ""


@app.route("/msg", methods=["POST"]) 
def upvote():
	send_msg = request.form["search"]
	send_post("https://webexapis.com/v1/messages", {"text": send_msg,"toPersonEmail": "answer_bot2@webex.bot"}, headers_post)
	time.sleep(2)
	send_post("https://webexapis.com/v1/messages", {"text": send_msg,"toPersonEmail": "answer_bot2@webex.bot"}, headers_post)
	answer_json = requests.get('https://webexapis.com/v1/messages/direct?personEmail=sender_bot1%40webex.bot', headers=headers_get).json()
	answer = answer_json['items'][1]['text']
	print(answer)
	return str(answer)


@app.route("/")
def index():
	return render_template("index.html")

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)



