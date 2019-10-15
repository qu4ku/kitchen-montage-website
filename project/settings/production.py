from .base import *
import os


DEBUG = False
ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ.get('SECRET_KEY'),

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get('NAME'),
#         'USER': os.environ.get('USER'),
#         'PASSWORD': os.environ.get('PASSWORD'),
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


MEDIA_ROOT = '/var/www/tyrantsthem/media/'
STATIC_ROOT = '/var/www/tyrantsthem/static/'

IS_MVP = True

# Conf for dropbox dbbackup
DBBACKUP_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
DBBACKUP_STORAGE_OPTIONS = {
    'oauth2_access_token': os.environ.get('DB_AUTH'),
}