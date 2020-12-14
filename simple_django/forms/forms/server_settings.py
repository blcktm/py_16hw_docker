import os

ALLOWED_HOSTS = [
     '127.0.0.1',
     # '45.94.157.160'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', ''),
        'USER': os.environ.get('POSTGRES_USER', ''),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
        'HOST': 'db',
    }
}

DEBUG = False
STATIC_ROOT = 'static_files'
