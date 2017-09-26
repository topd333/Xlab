# Django settings for xlab project.

import os
import logging
from oscar import get_core_apps
from oscar import OSCAR_MAIN_TEMPLATE_DIR
from oscar.defaults import *


DIRNAME = os.path.dirname(os.path.normpath(os.path.abspath(__file__)))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['linkinulife.com','www.linkinulife.com','144.76.18.178']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'



SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/srv/wsgi/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/srv/wsgi/static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #'/srv/wsgi/Xlab/xlab/static',
    os.path.join(DIRNAME, 'static'),   
    #'/home/cis/Desktop/linkidata/linki/xlab/static',

)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'oscar.apps.search.context_processors.search_form',
    'oscar.apps.promotions.context_processors.promotions',
    'oscar.apps.checkout.context_processors.checkout',
    'oscar.apps.customer.notifications.context_processors.notifications',
    'oscar.core.context_processors.metadata',

    # Required by allauth template tags
    "django.core.context_processors.request",
)



ROOT_URLCONF = 'xlab.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'xlab.mod_wsgi.application'


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(DIRNAME, 'templates'),
    OSCAR_MAIN_TEMPLATE_DIR,
)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.admindocs',
    'south',
    'keyedcache',
    'bidiutils',
    'django_ztask',
    'grid_user',
    'grid_welcome',
    'grid_help',
    'grid_guide',
    'api_auth',
    #'grid_profiles',
    'crispy_forms',
    'grid_core',
    'grid_estates',
    #'grid_staging',
    'compressor',
    'paypal',
    'grid_oxdata',
    'grid_space',
    'parsley',
    'account',

] + get_core_apps(['promotions'])

CRISPY_TEMPLATE_PACK = 'bootstrap'


CACHE_PREFIX = 'T'
CACHE_TIMEOUT = 300

AUTHENTICATION_BACKENDS=(
    'grid_user.backends.GridUserBackend',
    #'oscar.apps.customer.auth_backends.Emailbackend',
    #'django.contrib.auth.backends.ModelBackend',
)




LOGFILE = os.path.join(DIRNAME,'../xlab.log')

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename=LOGFILE,
    filemode='w')

logging.getLogger('django.db.backends').setLevel(logging.INFO)
logging.getLogger('keyedcache').setLevel(logging.INFO)
logging.getLogger('l10n').setLevel(logging.INFO)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

logging.info("Xlab Started")

from xlab.local_settings import *

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

LINKI_CURRENCY_RATE = 248


OSCAR_SHOP_NAME = 'Linkinulife'

OSCAR_DEFAULT_CURRENCY = 'USD'
OSCAR_CURRENCY_LOCALE = 'en'
OSCAR_CURRENCY_FORMAT = '### Ln'
OSCAR_FROM_EMAIL = 'shubhi.b@cisinlabs.com'


PAYPAL_API_USERNAME = 'shubhi.b001_api1.cisinlabs.com'
PAYPAL_API_PASSWORD = 'xxxxxxxxxxxxxxxxxxxxJ'
PAYPAL_API_SIGNATURE = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
PAYPAL_CURRENCY = 'USD'
PAYPAL_CALLBACK_HTTPS = False

OSCAR_DASHBOARD_NAVIGATION.append(
    {
        'label': 'PayPal',
        'icon': 'icon-globe',
        'children': [
            {
                'label': 'Express transactions',
                'url_name': 'paypal-express-list',
            },
        ]
    })

