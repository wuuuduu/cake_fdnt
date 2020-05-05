import os

from datetime import timedelta
from pathlib import Path

import raven
from django.utils.translation import gettext_lazy
from raven.exceptions import InvalidGitRepository
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django_filters',
    'raven.contrib.django.raven_compat',
    'django_cleanup.apps.CleanupConfig',
    'captcha',
    'rest_framework',
    'corsheaders',
]

PROJECT_APPS = [
    'cake',
]

INSTALLED_APPS = PROJECT_APPS + INSTALLED_APPS

LOGGING_DIR = os.path.join(Path(BASE_DIR).parent, 'logs')
LOGGING_LEVEL = 'INFO'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'cake_fdnt.middleware.XRealIPMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cake_fdnt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cake_fdnt.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation

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

# Internationalization

LANGUAGE_CODE = 'pl-PL'

LANGUAGES = (
    ('pl-PL', gettext_lazy('Polish')),
)

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, STATIC_URL[1:-1])
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'commons')
]

MEDIA_ROOT = os.path.join(Path(BASE_DIR).parent, 'media')
MEDIA_URL = '/media/'

# SHELL: usage ./manage.py shell_plus
SHELL_PLUS = 'ipython'
INTERNAL_IPS = [
    '127.0.0.1',
]

try:
    RELEASE = raven.fetch_git_sha(BASE_DIR)
except InvalidGitRepository:
    RELEASE = None

RAVEN_CONFIG = {
    'dsn': os.getenv('SENTRY_KEY'),
    'release': RELEASE,
    'environment': 'base',
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')

CORS_ORIGIN_WHITELIST = []

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
}

SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
