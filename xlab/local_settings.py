#import django.conf.global_settings as DEFAULT_SETTINGS
from .settings import *

import os
from django.utils.translation import ugettext as _

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DEBUG = True
TEMPLATE_DEBUG = DEBUG


ALLOWED_HOSTS = ['*']


ADMINS = (
    ('Admin User', 'jamesh@linkinulife.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'xlab_dev',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'django',
        'PASSWORD': 'xxxxxxxxxxxxx',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
        'ATOMIC_REQUESTS': True,
    },
    'oxdata': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'oxdata',
        'USER': 'txservice',
        'PASSWORD': 'xxxxxxxxxx,
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'ATOMIC_REQUESTS': True,
    },
    'grid_space': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'grid_space',
        'USER': 'django',
        'PASSWORD': 'xxxxxxxxxxxxxx',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'ATOMIC_REQUESTS': True,
    },
    'robust_grid': {
        'NAME': 'robust_grid',
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'USER': 'opensim',
        'PORT': '3306',
        'PASSWORD': 'xxxxxxxxxxxxxxxxx',
    },
    'estates': {
        'NAME': 'estates',
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'USER': 'os_estates',
        'PORT': '3308',
        'PASSWORD': 'xxxxxxxxxxxxxxx',
    },
}

DATABASE_ROUTERS = ['grid_db.dbhelper.SpaceRouter',
                    'grid_db.dbhelper.RobustGridRouter',                    
                    'grid_db.dbhelper.EstatesRouter',
                    #'grid_db.dbhelper.StagingRouter',
                    ]



# Make this unique, and don't share it with anybody.
SECRET_KEY = 'l$ykc444%f&s8dmqvcpsl29@pj8**3&abg$8+l*%(ad=&z*6jkh'

# Site Application
SITE_NAME = 'Linkinu'
SITE_TITLE = 'Linkinu'


# Welecome Application
WELCOME_HEADING = 'Linkinu'
WELCOME_TITLE = 'Linkinu'

# grid_user application
# Activation link, etc.
ACCOUNT_SERVER_ADDRESS = 'http://linkinulife.com'

LOGIN_URL = "/login"
AUTH_USER_MODEL = 'grid_user.User'
AUTH_SERVER_URL = 'http://linkinulife.com:8003'
ACCOUNT_SERVER_URL = 'http://linkinulife.com:8003'
ACCOUNT_ADMIN_EMAIL = 'jamesh@linkinulife.com'

XMLRPC_GATEWAY_IP = '144.76.18.178'


# Grid-Wide Estate Database Default Settings
ESTATE_DATABASE = 'estates'
ESTATE_DATASOURCE = 'linkinulife.com'
ESTATE_DATABASE_PORT = '3308'
ESTATE_DATABASE_USER = 'os_estates'
ESTATE_DATABASE_PASSWORD = 'xxxxxxxxxxxxxxxx'


# Default Estate Settings
DEFAULT_ESTATE_NAME = "Mainland"
DEFAULT_ESTATE_OWNER_NAME = "Governor LinkniU"


# Settings for grid user database for import.
USER_DATA_HOST = "127.0.0.1"
USER_DATA_USERNAME = "root"
USER_DATA_USERPASS = "xxxxxxxxxxxxxxxxxxxxxxxxx"
USER_DATA_DBNAME = "robust_grid"

# Settings for oxdata database for import.
OXDATA_DATA_HOST = "127.0.0.1"
OXDATA_DATA_USERNAME = "txservice"
OXDATA_DATA_USERPASS = "xxxxxxxxxxxxxxxxxxxx"
OXDATA_DATA_DBNAME = "oxdata"


LANGUAGES = (
    ('en', U'English'),
    ('ar', u'Arabic'),
    ('hi', u'Hindi'),
)


LOCALE_PATHS = (
    os.path.join(DIRNAME, '../locale')
)
