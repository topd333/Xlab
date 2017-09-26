from django.conf.urls import patterns, include, url
from account.views import profile

urlpatterns = patterns('',

    (r'^$', profile),
)
