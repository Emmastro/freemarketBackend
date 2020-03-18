import os
import dj_database_url
import django_heroku
from .base import*

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Connect to production database

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ALAMAU',
        'USER': 'emmamurairi',
        'PASSWORD': 'redolaemma!!123123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}"""

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   }
}

db_from_env  = dj_database_url.config(conn_max_age=1200, ssl_require=True)

DATABASES['default'].update(db_from_env)

# Use the statics and media from Amazon

#from .amazon_files import *

#--allow-unrelated-histories
# Security settings ** Set after getting the SSL certificate

CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = False
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False

django_heroku.settings(locals())


DEBUG = True

CORS_ORIGIN_WHITELIST = (
       'https://alamaufrontend.herokuapp.com',
)