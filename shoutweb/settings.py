"""
Django settings for shoutapp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# This was the Original...
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import os
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

from shoutweb import settings_local

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qvfv3eudl-qodwyot7%&%jc*v_rv)&fl&d5si9sna=sqq0ded8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shoutweb',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


DEBUG_TOOLBAR_PANELS = [
    # 'debug_toolbar.panels.versions.VersionsPanel',
    # 'debug_toolbar.panels.timer.TimerPanel',
    # 'debug_toolbar.panels.settings.SettingsPanel',
    # 'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    # 'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    # 'debug_toolbar.panels.templates.TemplatesPanel',
    # 'debug_toolbar.panels.cache.CachePanel',
    # 'debug_toolbar.panels.signals.SignalsPanel',
    # 'debug_toolbar.panels.logging.LoggingPanel',
    # 'debug_toolbar.panels.redirects.RedirectsPanel',
]


ROOT_URLCONF = 'shoutweb.urls'

WSGI_APPLICATION = 'shoutweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# STATIC_URL = '/static/'
ENV = settings_local.ENV

try:
    CSRF_FAILURE_VIEW = settings_local.CSRF_FAILURE_VIEW
except:
    pass

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/login/'
LOGOUT_URL = '/logout'

MEDIA_URL = '/upload/'

STATIC_ROOT = '' # django tiny mce requires this is set to something

try:
    MEDIA_ROOT = settings_local.MEDIA_ROOT
except:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'upload')

STATIC_URL = '/public/'

STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'public'),
)

try:
    TEMPLATE_DIRS = settings_local.TEMPLATE_DIRS
except:
    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'shoutweb', 'templates/'),
    )
