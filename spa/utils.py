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

def clean_data(text):
	try:
		if len(str(text)) > 0 and isinstance(text, str) == True:
			nlp = spacy.load('en_core_web_sm')
			nlp.max_length = 1500000
			stemmer = SnowballStemmer(language='english')
			text = remove_stopwords(text).lower()
			text = (re.sub("[^a-zA-Z]"," ",text)).rstrip().lstrip()
			return text
		else:
			return False
	except:
		return False


def get_data(df,text,query):
	try:
		if len(str(query)) > 0 and isinstance(query, str) == True and len(str(text)) > 0 and isinstance(text, list) == True:
			vectorizer = TfidfVectorizer()
			X = vectorizer.fit_transform(text)
			vectorizer.fit(text)
			vector = vectorizer.transform([query])
			results = cosine_similarity(X,vector).reshape((-1,))
			df['grades'] = results
			df = df.sort_values(by=['grades'], ascending=False)
			return df[['title','recommendations','artist','publisher','writer','genres','summary']].head(100)
		else:
			return False
	except:
		return False

def read_data(dataset):
	try:
		if len(str(dataset)) > 0 and isinstance(dataset, str) == True:
			df = pd.read_csv(dataset)
			return df
		else:
			return False
	except:
		return False

def execute_search(input_data,search_field,df):
	try:
		query = clean_data(input_data)
		if query != False:
			text = df[search_field].values.tolist()
			df = get_data(df,text,query)	
			return df
		else:
			return False
	except:
		return False

def generate_answer(query,df):
	try:
		if  len(query) > 0 and isinstance(query, str) == True and len(str(query)) > 0 and isinstance(query, str) == True: 
			df = execute_search(str(query),"clean_summary",df)	
			return str(df.title.values.tolist()[0]).replace('[','').replace(']','')+': '+str(df.summary.values.tolist()[0]).replace('[','').replace(']','')
		else:
			return False
	except:
		return False		


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
 


