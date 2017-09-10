# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator 
import re 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def validation(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Name needs to be at least 2 characters long!"
        if len(postData['alias']) < 2:
            errors['alias'] = "Alias needs to be at least 2 characters long!"
        if not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = 'Not a valid email!'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters long!'
        if postData['password'] != postData['confirm_password']:
            errors['password'] = 'Passwords do not match!'
        return errors

class User(models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)

class Review(models.Model):
    desc = models.TextField()
    rating = models.IntegerField()
    posted_on = models.DateField(auto_now_add=True)
    book = models.ForeignKey(Book, related_name='Book_Reviews')
    user = models.ForeignKey(User, related_name='User_Reviews')