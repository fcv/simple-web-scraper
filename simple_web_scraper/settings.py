"""
Django settings for simple_web_scraper project.

Generated by 'django-admin startproject' using Django 1.8.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import traceback

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')yl85h8y*n5hy8w&_j*sba&%bj9$ad0xmy@&d%q038xu)j90gy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'simple_web_scraper',
    'articles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'simple_web_scraper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'simple_web_scraper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
#
# uses 'DATABASE_URL' environment value to define Database connection when present.
# used in Heroku environment
import dj_database_url
if 'DATABASE_URL' in os.environ:
    # see examples of database urls at https://github.com/kennethreitz/dj-database-url/blob/afc4d3946c041ad0f5c70609a6d5e4e39ff54919/README.rst#url-schema
    DATABASES = {
        'default': dj_database_url.parse(os.environ['DATABASE_URL']),
    }
else:
    # https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
    # https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
    # http://stackoverflow.com/questions/5394331/how-to-setup-postgresql-database-in-django/5421511#5421511
    #
    # Note: this default values target GitLab's CI environment
    # In order to customize local environment's value use an untracked `simple_web_scraper/local_settings.py` file
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'web_scraper',
            'USER': 'web_scraper_user',
            'PASSWORD': 'web_scraper_pwd',
            'HOST': 'postgres',
            'PORT': '',
            'TEST': {
                'NAME': 'web_scraper_test'
            }
        }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# using custom local setting based on
# http://stackoverflow.com/questions/1626326/how-to-manage-local-vs-production-settings-in-django/1629770#1629770
# in the future other alternatives might be considered, like
#  - https://github.com/sobolevn/django-split-settings
try:
    from simple_web_scraper.local_settings import *
except ImportError as e:
    pass
