from django.conf.urls import patterns, include, url
from views import Welcome

urlpatterns = patterns('',
    url(r'^$', Welcome),
)
