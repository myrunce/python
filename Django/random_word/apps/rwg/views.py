# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    request.session['rwg'] = get_random_string(length=14)

    if request.method == 'POST':
        try:
            request.session['attempt'] += 1
        except:
            request.session['attempt'] = 1
        return redirect('/')

    return render(request, 'rwg/index.html')

def reset(request):
    request.session['attempt'] = 1
    return redirect('/')