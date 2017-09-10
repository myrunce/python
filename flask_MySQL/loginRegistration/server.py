from flask import Flask, render_template, request, redirect, flash, session
import re, md5
from mysqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app, 'login_registration')
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
        query = 'INSERT INTO users (first_name, last_name, email, hashed_password) VALUES(:a_first_name, :a_last_name, :a_email, :a_password)'
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
    if hashed_input == found_user[0]['hashed_password']:
        session['user_id'] = found_user[0]['id']
        session['user_name'] = found_user[0]['first_name'] + " " + found_user[0]['last_name']
        return redirect('/success')
    else:
        flash ('Invalid Login')
        return redirect ('/')

@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True)