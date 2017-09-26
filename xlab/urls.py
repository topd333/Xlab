from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static
# oscar
# from oscar.app import application

from app import application

from paypal.express.dashboard.app import application as paypal_app

import logging

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


log = logging.getLogger("[URL]: ")

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xlab.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^login/$', 'grid_user.views.login_user'),
    (r'^logout/$', 'grid_user.views.logout_user'),
    (r'^password/$', 'grid_user.views.user_password'),
    (r'^register/$', 'grid_user.views.register_user'),
    (r'^ajax_register/$', 'grid_user.ajax.ajax_register_user'),
    url(r'^ajax_accounttype/$', 'grid_user.ajax.ajax_accounttype_user', name='accounttype_registration'),
    (r'^activate', 'grid_user.views.activate_user'),
    (r'^welcome$', include('grid_welcome.urls')),
    (r'^help$', include('grid_help.urls')),
    (r'^about', 'grid_help.views.About'),
    (r'^guide$', include('grid_guide.urls')),
    (r'^account/', include('grid_user.urls')),
    url(r'^auth_api', include('api_auth.urls')),
    (r'^profile/$', 'grid_profiles.views.profile'),
    (r'^i18n/', include('django.conf.urls.i18n')),
    url(r'', include(application.urls)),
    (r'^checkout/paypal/', include('paypal.express.urls')),
    # Optional
    (r'^dashboard/paypal/express/', include(paypal_app.urls)),
    (r'^transaction/', include('grid_oxdata.urls')),
    (r'^disqus/', 'grid_oxdata.views.discusresponse'),
    (r'^flare$', 'grid_estates.views.flare'),
    (r'^join/$', 'grid_user.views.register_user'),
    url(r'^my/$', 'grid_user.mydeshbord.account_deshbord', name='my_deshbord'),
    url(r'^my/', include('account.urls'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns = [
#     # ... the rest of your URLconf goes here ...
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)