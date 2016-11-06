from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^search/$', views.search),
    url(r'^slow_search/$', views.slow_search),
]
