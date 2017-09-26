from django.conf.urls import patterns, include, url
from views import Guide

urlpatterns = patterns('',
    url(r'^$', Guide),
)
