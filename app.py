import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plate_number TEXT NOT NULL,
            location TEXT NOT NULL,
            image_path TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = get_db_connection()
    reports = conn.execute('SELECT * FROM reports ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', reports=reports)

@app.route('/report', methods=['POST'])
def report_car():
    plate_number = request.form.get('plate_number')
    location = request.form.get('location')
    file = request.files.get('image')

    if not plate_number or not location:
        flash("Please fill out all text fields.")
        return redirect(url_for('index'))

    filename = None
    if file and file.filename != '':
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO reports (plate_number, location, image_path) VALUES (?, ?, ?)',
        (plate_number, location, filename)
    )
    conn.commit()
    conn.close()

    flash("Report submitted successfully!")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
