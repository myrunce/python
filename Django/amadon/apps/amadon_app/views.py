# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    items = [{'name': "Dojo Tshirt", 'price': 19.99}, {'name': "Dojo Sweater", 'price': 29.99}, {'name': "Dojo Cup", 'price': 4.99}, {'name': "Algorithm Book", 'price': 49.99}]
    context = {
        'product_list': items
    }

    try:
        request.session['allItems']
    except:
        request.session['allItems'] = 0
    
    try: 
        request.session['gTotal']
    except:
        request.session['gTotal'] = 0

    return render(request, 'amadon_app/index.html', context)

def process(request):
    request.session['total'] = float(request.POST.get('price')) * float(request.POST.get('quantity'))
    request.session['allItems'] += int(request.POST.get('quantity'))
    request.session['gTotal'] += float(request.session['total']

    return redirect('/amadon/checkout')
        
def checkout(request):
    return render(request, 'amadon_app/checkout.html')

def back(request):
    return redirect('/amadon')