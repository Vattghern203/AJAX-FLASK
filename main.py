import sqlite3
from flask import Flask
from flask import render_template, jsonify, redirect, url_for
from flask import request

from time import time

from models import Manga

from dao import MangaDao


app = Flask(__name__)
app.secret_key = 'MANGABOY'

db = sqlite3.connect('database.db', check_same_thread=False)

manga_dao = MangaDao(db)


@app.route('/')
def index():
    
    if request.is_json:

        seconds = time()

        return jsonify({'seconds':seconds})

    return render_template('index.html')


@app.route('/add_manga', methods=['POST', 'GET'])
def add_manga():

    nome = request.form['nome']
    caps = request.form['caps']
    volumes = request.form['volumes']
    autor = request.form['autor']
    ano = request.form['ano']

    manga = Manga(nome, caps, volumes, autor, ano)

    manga_dao.add_manga(manga)

    results = {'processed': 'true'}

    return jsonify(results)

@app.route('/lista')
def lista():

    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
