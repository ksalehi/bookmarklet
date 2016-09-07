"""
Django settings for discoveryengine project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import six

from django.core.exceptions import ImproperlyConfigured

def get_env_var(var_name, default=None):
    """
    Get the environment variable VAR_NAME from the system,
    using the DEFAULT value if VAR_NAME is not found,
    and if no DEFAULT is provided, raising an error
    """
    
    def process_var_value(value):
        """
        Process the value of the environment variable,
        converting any boolean values into python booleans if needed,
        and returning other values as strings.
        """
        if isinstance(value, six.string_types):
            if value.lower() == 'true' or value == '1':
                return True
            if value.lower() == 'false' or value == '0':
                return False
        return value

    value = default

    try:
        value = process_var_value(os.environ[var_name])
    except KeyError:
        pass

    if value == None:
        raise ImproperlyConfigured("Environment variable %s is missing." % var_name)

    return value

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_var("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'rest_framework',
    'auth_disco',
    'discovery',
    'widget',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'discoveryengine.urls'

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

WSGI_APPLICATION = 'discoveryengine.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_env_var('DATABASE_NAME'),
        'USER': get_env_var('DATABASE_USER'),
        'PASSWORD': get_env_var('DATABASE_PASSWORD'),
        'HOST': get_env_var('DATABASE_HOST'),
        'PORT': get_env_var('DATABASE_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Social authentication
# http://psa.matiasaguirre.net/docs/configuration/django.html

AUTHENTICATION_BACKENDS = [
    'auth_disco.backends.orcid.ORCIDMemberOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Capsule Integration
CAPSULE_ID = get_env_var("CAPSULE_ID")
CAPSULE_API_KEY = get_env_var("CAPSULE_API_KEY")


# ORCID Integration
SOCIAL_AUTH_ORCID_MEMBER_KEY = get_env_var("ORCID_API_KEY")
SOCIAL_AUTH_ORCID_MEMBER_SECRET = get_env_var("ORCID_API_SECRET")
SOCIAL_AUTH_ORCID_MEMBER_SCOPE = ['/authenticate']
ORCID_API_KEY = get_env_var("ORCID_API_KEY")
ORCID_API_SECRET = get_env_var("ORCID_API_SECRET")
