from flask import Flask, render_template, request, flash, session
import re
import spacy
import flask
from flask import Flask, render_template, request, flash, session
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

app = Flask(__name__)

answer = ""
FILE = 'https://raw.github.com/elBichon/comic_search/master/site/final_clean_prod4.csv'
DF = utils.read_data(FILE)


@app.route("/msg", methods=["POST", "GET"]) 
def upvote():
	global DF
	df = utils.generate_answer(request.form["search"],DF)
	print(df)
	answer = df
	return answer



@app.route("/")
def index():
	return render_template("index.html")

