from flask import Flask, request, redirect, url_for, render_template, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'thisishellasecret'
mysql = MySQLConnector(app, 'my_friends')

@app.route('/')
def index():
    query = "SELECT * FROM friends"                          
    friends_from_db = mysql.query_db(query) 
    return render_template('index.html', friends = friends_from_db)

@app.route('/process', methods=['POST'])
def create():
    querystring = 'INSERT INTO friends (first_name, last_name, friend_since, year) VALUES (:first_name, :last_name, :friend_since, :year)'
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'friend_since': request.form['friend_since'],
        'year': request.form['year']
    }
    mysql.query_db(querystring, data)
    return redirect('/')
app.run(debug = True)