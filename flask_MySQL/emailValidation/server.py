from flask import Flask, render_template, flash, redirect, request, url_for
import re
from mysqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app, 'email_validation')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    else:
        flash("Success!")
        querystring = 'INSERT INTO emails (email, created_on) VALUES (:a_email, NOW())'
        data = {
            'a_email': request.form['email']
        }
        mysql.query_db(querystring, data)
        return redirect('/success')

@app.route('/success')
def success():
    query = "SELECT email, DATE_FORMAT(created_on, '%c/%e/%Y %r') AS created_on FROM emails"
    successEmails = mysql.query_db(query)
    return render_template('success.html', myEmails = successEmails)

app.run(debug=True)