from .base import *

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

WITWICKY = {
    'HOST' : '192.168.50.245:8080',
    'PATH' : '/token/',
    'METHOD' : 'GET',
}