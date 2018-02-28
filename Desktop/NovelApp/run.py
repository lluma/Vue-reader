from flask import Flask, render_template, jsonify, request
from random import *
from flask_cors import CORS
import urllib3
from bs4 import BeautifulSoup

app = Flask(__name__, static_folder = './dist/static', template_folder = './dist')
cors = CORS(app, resources={'/api/*': {'origins': '*'}})

http = urllib3.PoolManager()

@app.route('/api/contents')
def get_contents():
    res = http.request('GET', 'http://www.hjw.tw/0/2779/')
    soup = BeautifulSoup(res.data.decode('big5', 'ignore'))
    chapters = []
    for a in soup.find_all('a'):
        if a.text.count('章') > 0 and a['href'].count('html') > 0:
            chapters.append({
                'title' : a.text,
                'href' : a['href']
            })
    response = {
        'contents' : chapters
    }
    return jsonify(response)

@app.route('/api/article')
def get_article():
    href = request.args.get('href')
    path = 'http://www.hjw.tw' + href
    res = http.request('GET', path)
    soup = BeautifulSoup(res.data.decode('big5', 'ignore'))
    article = soup.find_all('div', 'article-con')
    splited_article = article[0].text.splitlines()
    response = {
        'article' : splited_article
    }
    return jsonify(response)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')
