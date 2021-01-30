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
#nlp = en_core_web_sm.load()
	nlp = spacy.load('en_core_web_sm')
	nlp.max_length = 1500000
	stemmer = SnowballStemmer(language='english')
	text = remove_stopwords(text).lower()
	text = (re.sub("[^a-zA-Z]"," ",text)).rstrip().lstrip()
	return text


def get_data(df,text,query):
	vectorizer = TfidfVectorizer()
	X = vectorizer.fit_transform(text)
	vectorizer.fit(text)
	vector = vectorizer.transform([query])
	results = cosine_similarity(X,vector).reshape((-1,))
	df['grades'] = results
	df = df.sort_values(by=['grades'], ascending=False)
	return df[['title','recommendations','artist','publisher','writer','genres','summary']].head(100)
def read_data(dataset):
	df = pd.read_csv(dataset)
	return df

def execute_search(input_data,search_field,df):
	query = clean_data(input_data)
	text = df[search_field].values.tolist()
	df = get_data(df,text,query)	
	return df


def generate_answer(query,df):
	df = execute_search(str(query),"clean_summary",df)	
	return str(df.title.values.tolist()[0]).replace('[','').replace(']','')+': '+str(df.summary.values.tolist()[0]).replace('[','').replace(']','')
			

