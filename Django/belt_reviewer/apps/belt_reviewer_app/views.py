# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages

# Create your views here.
def login_reg(request):
    return render(request, 'belt_reviewer_app/login_reg.html')

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
            created_user = User.objects.create(name = request.POST['name'], alias = request.POST['alias'] , email = request.POST['email'], password = passwordDB)
            request.session['user_id'] = created_user.id 
            request.session['user_name'] = created_user.name
            return redirect('/books')

def login(request):
    found_users = User.objects.filter(email = request.POST['email'])
    if found_users.count() > 0:
        found_user = found_users.first()
        if bcrypt.checkpw(request.POST['password'].encode(), found_user.password.encode()) == True:
            request.session['user_id'] = found_user.id 
            request.session['user_name'] = found_user.name
            return redirect('/books') 
        else:
            messages.error(request, 'Login Failed', extra_tags='fail')
            return redirect('/')
    else:
        messages.error(request, 'Login Failed', extra_tags='fail')
        return redirect('/')

def books(request):
    context = {
        'the_books': Book.objects.all(),
        "the_reviews": Review.objects.order_by('-id')[:3]
    }
    return render(request, 'belt_reviewer_app/books.html', context)

def add(request):
    context = {
        'the_authors': Book.objects.all()
    }
    return render(request, 'belt_reviewer_app/add.html', context)

def addbook(request):
    the_user = User.objects.get(id = request.session['user_id'])
    try:
        select_author = request.POST['select_author']
    except:
        select_author = ''
    typed_author = request.POST['author']

    if select_author == typed_author:
        new_book = Book.objects.create(title = request.POST['title'], author = select_author)
    elif typed_author == '':
        new_book = Book.objects.create(title = request.POST['title'], author = select_author)
    else:
        new_book = Book.objects.create(title = request.POST['title'], author = typed_author)
    
    new_review = Review.objects.create(desc = request.POST['review'], rating = request.POST['rating'], book = new_book, user = the_user)

    return redirect('/books')
    
def bookinfo(request, book_id):
    the_book = Book.objects.get(id = book_id)
    context = {
        'the_book': the_book,
        'the_reviews': Review.objects.filter(book = the_book)
    }

    return render(request, 'belt_reviewer_app/bookinfo.html', context)

def postReview(request):
    the_user = User.objects.get(id = request.session['user_id'])
    the_book = the_book = Book.objects.get(id = request.POST['book_id'])
    new_review = Review.objects.create(desc = request.POST['review'], rating = request.POST['rating'], book = the_book, user = the_user)

    return redirect('/books/' + request.POST['book_id'])

def userinfo(request, user_id):
    the_user = User.objects.get(id = user_id)
    context = {
        "the_user": the_user,
        "the_book_reviews": Review.objects.filter(user = the_user),
        "the_count": Review.objects.filter(user = the_user).count()
    }
    
    return render(request, 'belt_reviewer_app/userinfo.html', context)

def logout(request):
    del request.session['user_name']
    del request.session['user_id']
    messages.error(request, 'Logout Successful', extra_tags='logout')
    return redirect('/')

def delete(request, book_id, review_id):
    Review.objects.get(id = review_id).delete()
    return redirect('/books/' + book_id)
