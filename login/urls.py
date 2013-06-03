__author__ = 'arash'

from django.conf.urls import patterns, url

from login import views

urlpatterns = patterns('',
                       url(r'^$', views.login, name='login') ,
                       url(r'^close', views.logout , name='logout')
                       )