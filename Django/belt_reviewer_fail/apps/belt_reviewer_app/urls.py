from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^login$', views.login),
    url(r'^books$', views.books),
    url(r'^books/add$', views.add),
    url(r'^addbook$', views.addbook),
    url(r'^books/(?P<book_id>\d+)$', views.bookinfo),
]
