# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses_app/index.html', context)

def process(request):
    Course.objects.create(course_name = request.POST['name'], desc = request.POST['desc'])
    return redirect('/')

def destroy(request, course_id):
    the_course = Course.objects.get(id = course_id)
    context = {
        'course': the_course
    }
    return render(request, 'courses_app/destroy.html', context)

def delete(request, course_id):
    Course.objects.get(id = course_id).delete()
    return redirect('/')