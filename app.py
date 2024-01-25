import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    con = sqlite3.connect('chinook.db')
    con.row_factory = sqlite3.Row

    cursor = con.cursor()
    cursor.execute('''
        SELECT tracks.name as track_name, albums.Title as album_title, artists.name as artist_name
        FROM tracks
        INNER JOIN albums ON tracks.albumid = albums.albumid
        INNER JOIN artists ON albums.artistid = artists.artistid;
    ''')

    result = cursor.fetchall()
    con.close()

    return render_template('index.html', rows=result)
    
if __name__ == '__main__':
    app.run(debug=True)

