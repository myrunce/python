from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.login_reg),
    url(r'^process$', views.process),
    url(r'^login$', views.login),
    url(r'^books$', views.books),
    url(r'^books/add$', views.add),
    url(r'^addbook$', views.addbook),
    url(r'^books/(?P<book_id>\d+)$', views.bookinfo),
    url(r'^postReview$', views.postReview),
    url(r'^users/(?P<user_id>\d+)$', views.userinfo),
    url(r'^logout$', views.logout),
    url(r'^delete/(?P<book_id>\d+)/(?P<review_id>\d+)$', views.delete),
]