from flask import Flask, render_template, redirect, request, session, flash
import re 

app = Flask(__name__)
app.secret_key = "hellasecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    if len(request.form['first_name']) < 1:
        flash('First name cannot be left blank!')
    elif request.form['first_name'].isalpha() != True:
        flash('First name must not contain numbers!')
    else:
        flash('First name success!')
    
    if len(request.form['last_name']) < 1:
        flash('Last name cannot be left blank!')
    elif request.form['last_name'].isalpha() != True:
        flash('Last name must not contain numbers!')
    else:
        flash('Last name success!')
    
    if len(request.form['email']) < 1:
        flash('Email cannot be left blank!')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Please enter a valid email!')
    else:
        flash('Email success!')

    if len(request.form['password']) < 1:
        flash('Password cannot be left blank!')
    elif len(request.form['password']) < 8:
        flash('password needs to be larger than 8 characters!')
    else:
        flash('password success!')

    if len(request.form['confirm_password']) < 1:
        flash('Confirm password cannot be left blank!')    
    elif request.form['password'] != request.form['confirm_password']:
        flash('Passwords must match!')
    else:
        flash('Passwords match, success!')
    
    return redirect('/')

app.run(debug = True)