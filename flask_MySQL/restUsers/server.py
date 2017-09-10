from flask import Flask, render_template, request, redirect, flash, session
import re
from mysqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app, 'restusers')

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    usersQuery = 'SELECT * from users'
    users = mysql.query_db(usersQuery)
    return render_template('users.html', myUsers = users)

@app.route('/users/new')
def new():
    return render_template('new.html')

@app.route('/users/create', methods = ['POST'])
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

    if errors:
        return redirect('/users/new')
    else:
        query = 'INSERT INTO users (first_name, last_name, email, created_at) VALUES(:a_first_name, :a_last_name, :a_email, NOW())'
        data = {
            'a_first_name': request.form['first_name'],
            'a_last_name': request.form['last_name'],
            'a_email': request.form['email']
        }
        mysql.query_db(query, data)
        flash ('User added!')
        return redirect('/users')

@app.route('/users/<user_id>')
def info(user_id):
    infoQuery = "SELECT * FROM users WHERE users.id = " + user_id
    myInfo = mysql.query_db(infoQuery)
    return render_template('info.html', userInfo = myInfo)

@app.route('/users/<user_id>/edit')
def edit(user_id):
    currentID = user_id
    return render_template('edit.html', editID = currentID)

@app.route('/users/<user_id>', methods = ['POST'])
def editConfirm(user_id):
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
    
    if errors:
        return redirect('/users/<user_id>/edit')
    else:
        editQuery = 'UPDATE users SET first_name = :a_first_name, last_name = :a_last_name, email = :a_email WHERE users.id = :a_user_id'
        data = {
            'a_first_name': request.form['first_name'],
            'a_last_name': request.form['last_name'],
            'a_email': request.form['email'],
            'a_user_id': user_id
        }
        mysql.query_db(editQuery, data)
        return redirect ('/users/' + str(user_id))

@app.route('/users/<user_id>/destroy')
def delete(user_id):
    deleteQuery = 'DELETE FROM users WHERE id = ' + user_id
    mysql.query_db(deleteQuery)
    flash ('User Deleted!')
    return redirect ('/users')
app.run(debug=True)