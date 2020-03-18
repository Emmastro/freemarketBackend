import os

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', 'AKIATD722YS2VEQYAZ57') 
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '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')
AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_BUCKET', 'emmamurairi')

AWS_S3_FILE_OVERWRITE = True
AWS_DEFAULT = None
AWS_DEFAULT_ACL = None

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
#arn:aws:s3:::emmamurairi

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
