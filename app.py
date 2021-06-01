from logging import error
from re import DEBUG
from flask import Flask, redirect, request, render_template, app, url_for
from flask.helpers import flash
import requests
import urllib
from bs4 import BeautifulSoup
import operator

app = Flask(__name__)   
substring="https://en.wikipedia"

@app.route('/')  
def input():
    return render_template("form.html")

def start(url):    
    wordlist=[]
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')
   
    for each_text in soup.findAll('div', {'class':'mw-body'}):
        content = each_text.text
        words = content.lower().split()
	
        for each_word in words:
            wordlist.append(each_word)
    return clean_wordlist(wordlist)
            
def clean_wordlist(wordlist):
	clean_list = []
	for word in wordlist:
		symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "
		for i in range(len(symbols)):
			word = word.replace(symbols[i], '')

		if len(word) > 0:
			clean_list.append(word)
	return create_dictionary(clean_list)

def create_dictionary(clean_list):
    word_count = {}
    top_ten={}
    for word in clean_list:
        if word in word_count:
        	word_count[word] += 1
        else:
            word_count[word] = 1
    top_ten=sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_ten
    
@app.route('/output', methods =["GET", "POST"])
def output():
    if request.method == "POST":
        url = request.form.get("url")
        if substring in url:
            result = start(url)
        else:
            error="The url you entered is not of wikipedia! please enter a wikipedia url."
            return render_template("form.html", error=error)
    return render_template("form.html", result = result)

if __name__=='__main__':
   app.run(debug=True)