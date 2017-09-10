# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login_register_app/index.html')

def process(request):
    errors = User.objects.validation(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        found_users = User.objects.filter(email = request.POST['email'])
        if found_users.count() > 0:
            messages.error(request, 'Email already taken', extra_tags='email')
            return redirect('/')
        else:
            passwordDB = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            created_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'] , email = request.POST['email'], password = passwordDB)
            request.session['user_id'] = created_user.id 
            request.session['user_name'] = created_user.first_name 
            return redirect('/success')

def login(request):
    found_users = User.objects.filter(email = request.POST['email'])
    if found_users.count() > 0:
        found_user = found_users.first()
        if bcrypt.checkpw(request.POST['password'].encode(), found_user.password.encode()) == True:
            request.session['user_id'] = found_user.id 
            request.session['user_name'] = found_user.first_name
            return redirect('/success') 
        else:
            messages.error(request, 'Login Failed', extra_tags='fail')
            return redirect('/')
    else:
        messages.error(request, 'Login Failed', extra_tags='fail')
        return redirect('/')
def success(request):
    return render(request, 'login_register_app/success.html')