import os

from cake_fdnt.settings.base import *
from cake_fdnt.settings.logging import ConfigureLogger

DEBUG = True

SECRET_KEY = '111111111111111111111111111x111111111111111111111111'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cake_fdnt_local',
        'USER': 'cake_fdnt',
        'PASSWORD': 'cake_fdnt',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

LOGGING_DIR = os.path.join(BASE_DIR, 'logs')
LOGGING_LEVEL = 'DEBUG'

ConfigureLogger(log_level=LOGGING_LEVEL, logging_dir=LOGGING_DIR, django_modules=PROJECT_APPS)

INSTALLED_APPS += [
    'debug_toolbar',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# DISABLE SENTRY
RAVEN_CONFIG['dsn'] = ''
RAVEN_CONFIG['environment'] = 'local'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

RECAPTCHA_PUBLIC_KEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'  # FAKE, ALWAYS PASS
RECAPTCHA_PRIVATE_KEY = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'  # FAKE, ALWAYS PASS

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:4200',
    'http://localhost:4200',
]

try:
    from cake_fdnt.settings.local_settings import *
except ImportError:
    pass
