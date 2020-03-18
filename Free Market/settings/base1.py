import os

from django.core.wsgi import get_wsgi_application

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#MEDIA_ROOT = os.path.join('/media/')

INTERNAL_IPS = ['127.0.0.1']

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1','ALAMAUplatform.herokuapp.com','52.207.254.25']


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Main',
    'School',
    'Messaging',
    'Administration',
    'background_task',
    'bootstrap3',
    'django.contrib.admin',
    'django.contrib.postgres',
    'Team',
    'crispy_forms',
    'jet_django',

    'storages'
]

SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'ALAMAU.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['Main/template','School/template',"Accounts/template",
        "Accounts/template/registration"],
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


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
EMAIL_USE_TLS = True 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587 
EMAIL_HOST_USER = 'emmamurairi@gmail.com' 
EMAIL_HOST_PASSWORD = 'redolaemma' 
DEFAULT_FROM_EMAIL = 'emmamurairi@gmail.com'

WSGI_APPLICATION = 'ALAMAU.wsgi.application'


#JET_INDEX_DASHBOARD = 'Administration.dashboard.CustomIndexDashboard'

DATABASES = {'default': {'ATOMIC_REQUESTS': False,
             'AUTOCOMMIT': True,
             'CONN_MAX_AGE': 0,
             'ENGINE': 'django.db.backends.postgresql',
             'HOST': 'ALAMAU.cjmuyrtdpxml.us-east-1.rds.amazonaws.com',
             'NAME': 'ALAMAU',
             'OPTIONS': {},
             'PASSWORD': 'redolaemma!!123123',
             'PORT': '5432',
             'TEST': {'CHARSET': None,
                      'COLLATION': None,
                      'MIRROR': None,
                      'NAME': None},
             'TIME_ZONE': None,
             'USER': 'emmamurairi'}
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'ALAMAU',
#         'USER' : 'emmanuel',
#         'PASSWORD' : 'redolaemma@@123',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',#'63068',
#     }
# }
#http://127.0.0.1:63068/?key=8311d41b-5a8b-4d01-b9cf-33ab74411547

#DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


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

CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False


#CSRF_FAILURE_VIEW
CRISPY_FAIL_SILENTLY = not DEBUG

CRISPY_TEMPLATE_PACK = 'bootstrap4'
#CRISPY_TEMPLATE_PACK = 'uni_form'

LOGIN_REDIRECT_URL = 'home'

#Amazon Config

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', 'AKIATD722YS22J4JT4OI')#AKIATD722YS2XW3FYMZG') 
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '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')#ub3L9MZeG+T0LBjV+aALhQu3FhEHcIls0DO9fdU6oUl3')#SqRe1DOgUIEaw5/tWjFeH7GJ8UODpXyIYDGh')
AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_BUCKET', 'emmamurairi')

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT = None
AWS_DEFAULT_ACL = None

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
#arn:aws:s3:::emmamurairi

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, 'media')

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

# the sub-directories of media and static files
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'


STATICFILES_STORAGE = 'ALAMAU.custom_storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'ALAMAU.custom_storages.MediaStorage'

#STATIC_URL = '/static/'
#MEDIA_URL = '/media/'
SECRET_KEY = os.environ.get('SECRET_KEY', '8fb+7(lo=syt)u16-lo$2_5f*$7i(o(ufy2ymyh22ql8&9gvhtw')