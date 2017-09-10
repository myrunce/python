# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import randrange
import datetime
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
	try:
		request.session['gold']
		print "I have gold already"
	except KeyError:
		request.session['gold'] = 0
	try:
		request.session['messages']
	except KeyError:
		request.session['messages'] = []
	return render(request, 'gold_app/index.html')

def process(request):
    location = request.POST.get('building')
    if location == "farm":
	    gold_earned = randrange(10,21)
    elif location == "cave":
	    gold_earned = randrange(5,11)
    elif location == "house":
	    gold_earned = randrange(2,6)
    elif location == "casino":
	    gold_earned = randrange(-50,50)
	
    request.session['gold'] += gold_earned
    if gold_earned < 0:
	    color = "red"
	    new_string = "Went to casino and lost "+str(-gold_earned)+ " gold. Ouch! "+str(datetime.datetime.now()) 
    else:
	    color = "green"
	    new_string = "Went to "+location+" and got "+str(gold_earned)+" gold. "+str(datetime.datetime.now())
    new_dictionary = {
    "color":color,
    "message":new_string
    }
    request.session['messages'].insert(0,new_dictionary)
    request.session.modified = True
    return redirect('/')