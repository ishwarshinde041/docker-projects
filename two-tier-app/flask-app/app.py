# app.py
from flask import Flask, render_template, request, redirect, URL_For 
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'test',
    'password': 'test@123',
    'database': 'flask_app'
}

# Connect to MySQL
db = mysql.connector.connect(**db_config)
cursor = db.cursor()

@app.route('/')
def index():
    # Fetch data from the database
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    email = request.form['email']

    # Insert data into the database
    cursor.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (username, email))
    db.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

