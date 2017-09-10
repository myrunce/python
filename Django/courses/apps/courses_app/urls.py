from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^destroy/(?P<course_id>\d+)$', views.destroy),
    url(r'^confirmDelete/(?P<course_id>\d+)$', views.delete),
]