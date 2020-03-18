import os
from django.core.wsgi import get_wsgi_application
import django_heroku

from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

INTERNAL_IPS = ['127.0.0.1']


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders  . .
    # ---'compressor.finders.CompressorFinder',
)

DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize', # Make content look more human
    #'sorl.thumbnail', # For optimisation 
    #"compressor", # Compress css and js for optimisation
    'Accounts',    
    'Main',
    'Inbox',
    'django.contrib.admin',
    #'django.contrib.postgres',
    'Help',
    'rest_framework',
    'corsheaders',
]

SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'FreeMarket.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [
        #],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        
        },
    },
]

# Send with African Libraries mail address

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
#EMAIL_USE_TLS = True 
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = 'emmamurairi@gmail.com' 
#EMAIL_HOST_PASSWORD = 'redolaemma##123' 


AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_SES_REGION_NAME = 'us-east-1'
AWS_SES_REGION_ENDPOINT = 'email-smtp.us-east-1.amazonaws.com'

EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'

EMAIL_PORT = 465

EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ""
DEFAULT_FROM_EMAIL = ''

EMAIL_USE_SSL = True
#EMAIL_USE_TLS = True

WSGI_APPLICATION = 'FreeMarket.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

ADMINS = (
    ('Emmastro', 'emurairi18@alastudents.org'),
)

MANAGERS = ADMINS

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOGIN_URL = '/accounts/login/'

LOGIN_REDIRECT_URL = 'home'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Overwrite the AWS Settings
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
SECRET_KEY = os.environ.get('SECRET_KEY', '8fb+7(lo=syt)u16-lo$2_5f*$7i(o(ufy2ymyh22ql8&9gvhtw')

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

# Site constant
SITE_TITLE = 'Free Market'

PUSH_NOTIFICATIONS_SETTINGS = {
        "FCM_API_KEY": "AIzaSyBdxS0kL7mvEmki_hk4p0Z3J1lYQ66BDSs", # Fire cloud messaging for Google
       }

# Allow Cross request from React
CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
       'http://localhost:3000',
       'https://freemarket.herokuapp.com',
)



'''
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}'''

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}