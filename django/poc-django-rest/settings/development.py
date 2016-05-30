from .base import *

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'dev.db',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#     }
# }

URL_TESTE = 'DEV'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'poc',
        'USER': 'poc',
        'PASSWORD': '$Pocdjango2016$',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}




