from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'authorize', 'api_auth.views.authorize'),
)
