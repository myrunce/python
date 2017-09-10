# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'belt_reviewer_app/index.html')

def process(request):
    errors = User.objects.validation(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        found_users_email = User.objects.filter(email = request.POST['email'])
        found_users_alias = User.objects.filter(alias = request.POST['alias'])
        if found_users_email.count() > 0:
            messages.error(request, 'Email already taken', extra_tags='email')
            return redirect('/')
        elif found_users_alias.count() > 0:
            messages.error(request, 'Alias already taken', extra_tags='alias')
            return redirect('/')
        else:
            passwordDB = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            created_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], alias = request.POST['alias'], email = request.POST['email'], password = passwordDB)
            request.session['user_id'] = created_user.id 
            request.session['user_name'] = created_user.first_name 
            messages.error(request, 'Register Success! You may login.')
            return redirect('/')

def login(request):
    found_users = User.objects.filter(email = request.POST['email'])
    if found_users.count() > 0:
        found_user = found_users.first()
        if bcrypt.checkpw(request.POST['password'].encode(), found_user.password.encode()) == True:
            request.session['user_id'] = found_user.id 
            request.session['user_name'] = found_user.first_name
            return redirect('/books') 
        else:
            messages.error(request, 'Login Failed', extra_tags='fail')
            return redirect('/')
    else:
        messages.error(request, 'Login Failed', extra_tags='fail')
        return redirect('/')

def books(request):
    return render(request, 'belt_reviewer_app/books.html')

def add(request):
    return render(request, 'belt_reviewer_app/add.html')

def addbook(request):
    the_user = User.objects.get(id = request.session['user_id'])
    if request.POST['author'] != None:
        new_author = Author.objects.create(name = request.POST['author'])
        new_book = Book.objects.create(name = request.POST['book_name'], rating = request.POST['rating'], User = the_user, Author = new_author)
    else:
        found_author = Author.objects.get(name = request.POST['select_author'])
        new_book = Book.objects.create(name = request.POST['book_name'], rating = request.POST['rating'], User = the_user, Author = found_author)

    new_review = Review.objects.create(desc = request.POST['review'], User = the_user, Book = new_book)
    return redirect('/books/' + new_book.id)

def bookinfo(request, book_id):
    the_book = Book.objects.get(id = book_id)
    context = {
        'the_book': the_book,
        'the_author': Author.objects.get(id = the_book.author_id),
        'the_reviews':Author.objects.get(book_id = book_id)
    }
    return render(request, 'belt_reviewer_app/bookinfo.html')