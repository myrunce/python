import random, datetime
from flask import Flask, render_template, request, redirect, session, url_for 
app = Flask(__name__)

app.secret_key = "Hellasecret"

@app.route('/')
def landing_page():
    try:
        session['gold']
        print "I have gold already"
    except KeyError:
        session['gold'] = 0
    try:
        session['messages']
    except KeyError:
        session['messages'] = []
    return render_template('index.html')

@app.route('/process_money', methods =['POST'])
def process():
    print request.form['building']
    location = request.form['building']
    if location == 'farm':
        gold_earned = random.randrange(10,21)
    elif location == "cave":
        gold_earned = random.randrange(5,11)
    elif location == "house":
        gold_earned = random.randrange(2,6)
    elif location == "casino":
        gold_earned = random.randrange(-50,50)
    session['gold'] += gold_earned

    if gold_earned < 0:
        color = "red"
        message = "Entered a casino and lost " + str(-gold_earned) + " gold...ouch " + str(datetime.datetime.now())
    else: 
        color = "green"
        message = "Earned " + str(gold_earned) + " gold from the " + location + "! " + str(datetime.datetime.now())

    new_dictionary = {
        "color":color,
        "message":message
    }

    print "***********"
    print "THIS IS THE DICTIONARY", new_dictionary
    print "***********"  
    session['messages'].insert(0, new_dictionary)  
    print "THIS IS THE GOLD EARNED", gold_earned
    print "***********"    
    print "THIS IS SESSION[MESSAGES]",session['messages']
    print "***********"    
    return redirect('/')

app.run(debug = True)