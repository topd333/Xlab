from django.conf.urls import patterns, include, url
from account.views import user, change_password, change_email
from ajax import ajax_checkusername


urlpatterns = patterns('',

    (r'^$', user),
    (r'^preferences/$', user),
    (r'^change_password', change_password),
    (r'^change_email', change_email),
    (r'^ajax/ajax_checkusername', ajax_checkusername),
    url(r'^ajax/ajax_checkpassword', 'grid_user.ajax.ajax_checkpassword', name='ajax-check-password'),
    )
