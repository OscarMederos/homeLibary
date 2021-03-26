import flask
from flask import request, jsonify
import sqlite3
import csv

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Home Library API 1.0</h1>
<p>A prototype API for Home Library.</p>'''

@app.route('/api/v1/resources/videogames/all', methods=['GET'])
def api_all():
    con = sqlite3.connect('videogames.db')
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute("CREATE TABLE videogames(id INTEGER PRIMARY KEY AUTOINCREMENT, platform TEXT, tittle TEXT, publisher TEXT)")
    with open('videogames.csv', 'r') as fin:
        dr = csv.reader(fin)
        to_db = []
        for line in dr:
            to_db.append(line)

    cur.executemany("INSERT INTO videogames(platform, tittle, publisher) VALUES(?, ?, ?)", to_db)
    con.commit()
    
    all_videogames = cur.execute('SELECT * FROM videogames;').fetchall()

    return jsonify(all_videogames)

@app.route('/api/v1/resources/videogames', methods=['GET'])
def api_filter():
    query_parameters = request.args

    platform = query_parameters.get('platform')
    tittle = query_parameters.get('tittle')
    publisher= query_parameters.get('publisher')

    query = "SELECT * FROM videogames WHERE"
    to_filter = []

    if platform:
        query += ' platform=? AND'
        to_filter.append(platform)
    if tittle:
        query += ' tittle=? AND'
        to_filter.append(tittle)
    if publisher:
        query += ' publisher=? AND'
        to_filter.append(publisher)
    if not (platform or tittle or publisher):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('videogames.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()