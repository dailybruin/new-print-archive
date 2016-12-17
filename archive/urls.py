from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^originaloverlay/$', views.loadOriginalOverlay),
    url(r'^search/', views.search),
    url(r'^slow_search/', views.slow_search),
    url(r'^overlay/(?P<decade>[0-9]{4})/$', views.getYear),    
    url(r'^overlay/(?P<decade>[0-9]{4})/(?P<year>[0-9]{4})$', views.getMonths),
    url(r'^overlay/(?P<decade>[0-9]{4})/(?P<year>[0-9]{4})/(?P<month>[1-9]{1}|10|11|12)/$', views.getDays),
    url(r'^overlay/(?P<decade>[0-9]{4})/(?P<year>[0-9]{4})/(?P<month>[1-9]{1}|10|11|12)/(?P<day>(1|2|3)?[0-9]{1})/$', views.showContent),
]
