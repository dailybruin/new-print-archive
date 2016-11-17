from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^search/', views.search),
    url(r'^slow_search/', views.slow_search),
    url(r'^overlay/(?P<year>[0-9]{4})/$', views.getYear),

]
