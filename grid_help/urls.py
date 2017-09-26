from django.conf.urls import patterns, include, url
from views import Help, About

urlpatterns = patterns('',
    url(r'^$', Help),
    url(r'^about', About),
)
