from flask import Flask, url_for, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<ninja_color>')
def show_ninja(ninja_color):
    if ninja_color == 'red' or ninja_color == 'blue' or ninja_color == 'orange' or ninja_color == 'purple': 
        return render_template(''+ ninja_color +'.html')
    else:
        return redirect('/notNinja')

@app.route('/notNinja')
def notNinja():
    return render_template('notapril.html')

app.run(debug = True)
