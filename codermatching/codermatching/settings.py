"""
Django settings for codermatching project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import django_heroku
import os
import re

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SEC_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    # 'codermatch.apps.CodermatchConfig',
    'codermatch', #this works because the name is defined in codermatch.apps.CodermatchConfig
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',  # to activate 404 error sending to MANAGERS; based on https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/#admins-and-managers & https://docs.djangoproject.com/en/4.0/howto/error-reporting/#errors
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'codermatching.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates' #alternative with same meaning: os.path.join(BASE_DIR, 'templates')
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

WSGI_APPLICATION = 'codermatching.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': '127.0.0.1',
        'PORT': '',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
# https://docs.djangoproject.com/en/4.0/howto/deployment/

STATIC_URL = 'static/'

# STATIC_ROOT = "/var/www/example.com/static/"  # based on: https://docs.djangoproject.com/en/4.0/howto/static-files/#deployment & https://docs.djangoproject.com/en/4.0/howto/static-files/deployment/#serving-static-files-in-production > https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-STATIC_ROOT

# STATICFILES_STORAGE = 'codermatching.storage.S3Storage'   # based on: https://docs.djangoproject.com/en/4.0/howto/static-files/#configuring-static-files > https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-STATICFILES_STORAGE > https://docs.djangoproject.com/en/4.0/howto/static-files/deployment/#staticfiles-from-cdn

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- NON-DEFAULT SETTINGS ---

# Email settings
# Tutorials: https://www.sitepoint.com/django-send-email/#usingdjangoenvirontohidesensitivekeys & https://medium.com/@_christopher/how-to-send-emails-with-python-django-through-google-smtp-server-for-free-22ea6ea0fb8e
# environment variables: https://www.youtube.com/watch?v=IolxqkL7cD8
# email settings (start): https://docs.djangoproject.com/en/4.0/ref/settings/#email-backend

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['EMAIL_HOST_NAME']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_PW']
EMAIL_HOST_USER = os.environ['EMAIL_USER']
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Email reports and Server errors: https://docs.djangoproject.com/en/4.0/howto/error-reporting/#email-reports
ADMINS = [('CoderMatching', os.environ['MAIN_MAIL_ADDRESS']),]  # people being notified with email reports (like 500 errors): https://docs.djangoproject.com/en/4.0/howto/error-reporting/#email-reports
MANAGERS = [('CoderMatching', os.environ['MAIN_MAIL_ADDRESS']),] # people being notified with email reports (like 404 errors): https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/#admins-and-managers
SERVER_EMAIL = os.environ['MAIN_MAIL_ADDRESS']

DEFAULT_FROM_EMAIL = os.environ['MAIN_MAIL_ADDRESS']

IGNORABLE_404_URLS = [
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
]

# HTTPS https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/#https
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Configuring Django Apps for Heroku
# https://devcenter.heroku.com/articles/django-app-configuration#settings-py-changes
# Activate Django-Heroku.
django_heroku.settings(locals())