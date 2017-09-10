from flask import Flask, render_template, request, redirect, flash, session
import re, md5
from mysqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app, 'the_wall')
salt = "notsecure"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registering', methods = ['POST'])
def register():
    errors = False
    if len(request.form['first_name']) < 2:
        flash('First name must be longer than 2 characters!')
        errors = True
    if not request.form['first_name'].isalpha():
        flash('First name must not contain numbers!')
        errors = True
    if len(request.form['last_name']) < 2:
        flash('Last name must be longer than 2 characters!')
        errors = True
    if not request.form['last_name'].isalpha():
        flash('Last name must not contain numbers!')
        errors = True
    if not re.match(EMAIL_REGEX, request.form['email']):
        flash('Not a valid email!')
        errors = True
    if len(request.form['password']) < 8:
        flash('password must be at least 8 characters!')
        errors = True
    if request.form['password'] != request.form['confirm_password']:
        flash('passwords must match!')
        errors = True

    if errors:
        return redirect('/')
    else:
        hashedpassword = md5.new(salt+request.form['password']).hexdigest()
        query = 'INSERT INTO users (first_name, last_name, email, password) VALUES(:a_first_name, :a_last_name, :a_email, :a_password)'
        data = {
            'a_first_name': request.form['first_name'],
            'a_last_name': request.form['last_name'],
            'a_email': request.form['email'],
            'a_password': hashedpassword
        }
        mysql.query_db(query, data)
        flash ('Registration Success')
        return redirect('/')

@app.route('/process', methods = ['POST'])
def process():
    loginquery = "SELECT * FROM users WHERE email = :user_email"
    data = {
        'user_email':request.form['email']
    }
    found_user = mysql.query_db(loginquery, data)
    hashed_input = md5.new(salt+request.form['password']).hexdigest()
    if hashed_input == found_user[0]['password']:
        session['user_id'] = found_user[0]['id']
        session['user_name'] = found_user[0]['first_name'] + " " + found_user[0]['last_name']
        return redirect('/wall')
    else:
        flash ('Invalid Login')
        return redirect ('/')

@app.route('/wall')
def success():
    messagequery = "SELECT users.id as person, users.first_name, users.last_name, messages.id, messages.message, messages.updated_at, messages.user_id FROM users JOIN messages"
    myMessage = mysql.query_db(messagequery)
    commentquery = 'SELECT users.first_name, users.last_name, messages.id, comments.message_id, comments.comment, comments.created_at FROM comments JOIN messages ON messages.id = comments.message_id LEFT JOIN users ON users.id = comments.user_id'
    myComment = mysql.query_db(commentquery)
    return render_template('wall.html', messages = myMessage, comments = myComment)

@app.route('/postmessage', methods = ['POST'])
def postmessage():
    postquery = 'INSERT INTO messages (message, created_at, updated_at, user_id) VALUES(:a_message, NOW(), NOW(), :a_user_id)'
    data = {
        'a_message':request.form['post_message'],
        'a_user_id':session['user_id']
    }
    mysql.query_db(postquery, data) 
    return redirect('/wall')

@app.route('/postcomment', methods = ['POST'])
def postcomment():
    commentquery = 'INSERT INTO comments (comment, created_at, updated_at, user_id, message_id) VALUES (:a_comment, NOW(), NOW(), :a_user_id, :a_message_id)'
    data = {
        'a_comment': request.form['post_comment'],
        'a_user_id': session['user_id'],
        'a_message_id': request.form['hidden_id']
    }
    mysql.query_db(commentquery, data)
    return redirect('/wall')

@app.route('/logoff')
def logoff():
    session.clear()
    return redirect('/')

app.run(debug=True)