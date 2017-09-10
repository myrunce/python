# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render (request, 'surveyform/index.html')

def result(request):
    context = {
        'name': request.POST.get('name'),
        'location': request.POST.get('location'),
        'language': request.POST.get('language'),
        'comment': request.POST.get('comment')
    }
    try: 
        request.session['counter'] +=1
    except:
        request.session['counter'] = 1
    return render(request, 'surveyform/results.html', context)