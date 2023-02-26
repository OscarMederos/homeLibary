import csv
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/games')
def get_games():
    try:
        query_parameters = request.args

        platform = query_parameters.get('platform')
        title = query_parameters.get('title')
        publisher = query_parameters.get('publisher')

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        query = "SELECT * FROM library WHERE"
        to_filter = []

        if platform:
            query += ' platform=? AND'
            to_filter.append(platform)
        if title:
            query += ' title=? AND'
            to_filter.append(title)
        if publisher:
            query += ' publisher=? AND'
            to_filter.append(publisher)
        if not (platform or title or publisher):
            return page_not_found(404)

        query = query[:-4] + ';'

        results = cursor.execute(query, to_filter).fetchall()

        games = []
        for row in results:
            game = {'id': row[0], 'platform': row[1], 'title': row[2], 'publisher': row[3]}
            games.append(game)

        return jsonify(games)

    except Exception:
        return 'Internal Server Error', 500

if __name__ == '__main__':
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS library")
    cursor.execute("CREATE TABLE library (id INTEGER PRIMARY KEY, platform TEXT, title TEXT, publisher TEXT)")

    with open('library.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader) # skip header row
        for row in reader:
            cursor.execute("INSERT INTO library (platform, title, publisher) VALUES (?, ?, ?)", row)

    conn.commit()

    app.run(debug=False)
