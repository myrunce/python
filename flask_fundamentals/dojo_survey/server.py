from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "hellasecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def process():
    name = request.form['name']
    if len(name) < 1:
        flash('name cannont be blank!')
    location = request.form['dojoLocation']
    favorite_language = request.form['favLanguage']
    comment = request.form['comment']
    if len(comment) > 120:
        flash('please shorten your comment! 120 chars or less')
    elif len(comment) < 1:
        flash('comment area cannot be blank!')
    return render_template('result.html', name = name, location = location, favorite_language = favorite_language, comment = comment)

app.run(debug = True)

