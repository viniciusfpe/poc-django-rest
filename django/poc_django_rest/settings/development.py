from .base import *

# Database
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

WITWICKY = {
    'HOST' : '192.168.50.245:8080',
    'PATH' : '/token/',
    'METHOD' : 'GET',
}
