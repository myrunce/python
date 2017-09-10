from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^checkout', views.checkout),
    url(r'^process', views.process),
    url(r'^back', views.back)
]