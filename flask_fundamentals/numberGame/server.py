import random
from flask import Flask, redirect, request, session, render_template, url_for

app = Flask(__name__)
app.secret_key = "hellasecret"

@app.route('/')
def index():
    try:
        session['randomNum']
    except KeyError:
        session['randomNum'] = random.randrange(0,100)
    try:
        session['guesses'] 
    except KeyError: 
        session['guesses'] = []    
    # print '********'
    # print "THIS NUMBER IS THE NUMBER TO GUESS", session['randomNum']
    # print '********'
    print "THIS IS THE INFO I WANT IN HTML", session['guesses']
    return render_template('index.html')
    
@app.route('/process', methods=['POST'])
def process():
    guess = int(request.form['guess'])
    print '********'
    print "THIS IS THE GUESS", guess
    print session['randomNum']
    print session['randomNum'] == guess
    if guess > session['randomNum']:
        color = 'red'
        new_string = 'You guessed too high!'
        print new_string
    elif guess < session['randomNum']:
        color = 'red'
        new_string = "You guessed too low!"
        print new_string
    else:
        color = 'green'
        new_string = "You guessed correct you clever animal!"
        print new_string

    guess_dict = {
        "color": color,
        "message": new_string
    }
    print "THIS IS GUESS DICT", guess_dict
    session['guesses'] = guess_dict
    print "*******"
    print "THIS IS THE INFO I WANT IN SESSION[GUESSES]", session['guesses']
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)