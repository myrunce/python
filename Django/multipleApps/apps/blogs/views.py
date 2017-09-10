# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "Index/Blogs Placeholder handled by blogs!!"
    return HttpResponse(response)

def new(request):
    response = "Blogs/new placeholder handled by blogs!"
    return HttpResponse(response)

def create(request):
    return redirect('/blogs')

def number(request, number):
    response = "You are on blog #" + number
    return HttpResponse(response)

def edit(request, number):
    response = "You are editing blog #" + number
    return HttpResponse(response)

def delete(request, number):
    return redirect('/blogs')