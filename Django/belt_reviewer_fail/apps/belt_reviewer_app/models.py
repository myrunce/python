# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator 
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class BlogManager(models.Manager):
    def validation(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name needs to be at least 2 characters long!"
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name needs to be at least 2 characters long!'
        if not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = 'Not a valid email!'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters long!'
        if postData['password'] != postData['confirm_password']:
            errors['password'] = 'Passwords do not match!'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    objects = BlogManager()

class Author(models.Model):
    name = models.CharField(max_length = 255, unique=True)
    objects = BlogManager()

class Book(models.Model):
    name = models.CharField(max_length = 255)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5),])
    Author = models.ForeignKey(Author, related_name='books')
    objects = BlogManager()
    

class Review(models.Model):
    desc = models.TextField()
    User = models.ForeignKey(User, related_name='Reviews')
    Book = models.ForeignKey(Book, related_name='Reviews')
    objects = BlogManager()