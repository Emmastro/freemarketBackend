import os
import dj_database_url
from .base import*
CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False

#django_heroku.settings(locals())

# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.postgresql',
#          'NAME': 'ALAMAU',
#          'USER' : 'emmamurairi',
#          'PASSWORD' : 'redolaemma!!123123',
#          'HOST': '127.0.0.1',
#          'PORT': '5432',#'63068',
#      }
# }
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   }
}

CSRF_COOKIE_HTTPONLY = False

#from .amazon_files import *