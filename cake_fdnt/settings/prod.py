from cake_fdnt.settings.logging import ConfigureLogger
from .base import *

ConfigureLogger(log_level=LOGGING_LEVEL, logging_dir=LOGGING_DIR, django_modules=PROJECT_APPS)

SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASES_NAME'),
        'USER': os.getenv('DATABASES_USER'),
        'PASSWORD': os.getenv('DATABASES_PASSWORD'),
        'HOST': os.getenv('DATABASES_HOST'),
        'PORT': os.getenv('DATABASES_PORT'),
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
    'rest_framework.renderers.JSONRenderer',
]

ALLOWED_HOSTS = [
    'api.tort.fdntkrakow.pl'
]

RAVEN_CONFIG['environment'] = 'prod'

CORS_ORIGIN_WHITELIST = [
    'https://tort.fdntkrakow.pl',
    'https://www.tort.fdntkrakow.pl'
]
