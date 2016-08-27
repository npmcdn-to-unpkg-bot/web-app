"""
Django settings for web_appapp project.

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

from web_app import settings_local

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
    'web_app',
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
    # 'debug_toolbar.panels.templates.TemplatesPanel'
    # 'debug_toolbar.panels.cache.CachePanel',
    # 'debug_toolbar.panels.signals.SignalsPanel',
    # 'debug_toolbar.panels.logging.LoggingPanel',
    # 'debug_toolbar.panels.redirects.RedirectsPanel',
]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    # 'django.core.context_processors.debug',
    # 'django.core.context_processors.i18n',
    # 'django.core.context_processors.media',
    # 'django.core.context_processors.static',
    # 'django.core.context_processors.tz',
    'django.template.context_processors.debug',
    'django.template.context_processors.i18n',
    'django.template.context_processors.media',
    'django.template.context_processors.static',
    'django.template.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.template.context_processors.request',
)


ROOT_URLCONF = 'web_app.urls'

WSGI_APPLICATION = 'web_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
try:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#             'NAME': 'web_app1db',
#             'USER': 'root',
#             'PASSWORD': '',
#             'HOST': 'localhost',
#             'PORT': '3306',
#         },
#     }
# except:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
except:
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
        os.path.join(BASE_DIR, 'web_app', 'templates/'),
    )


try:
    LOGGING = settings_local.LOGGING
except:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '[%(asctime)s] [%(levelname)s] [%(module)s:%(lineno)s] %(message)s'
            },
            'tracer': {
                'format': '[%(asctime)s] [TRACE] %(message)s'
            },
        },
        # 'filters': {
        #     'require_debug_false': {
        #         '()': 'django.utils.log.RequireDebugFalse'
        #     }
        # },
        'handlers': {
            # 'mail_admins': {
            #     'level': 'ERROR',
            #     'filters': ['require_debug_false'],
            #     'class': 'django.utils.log.AdminEmailHandler'
            # },
            'console': {
                'level':'DEBUG',
                'class':'logging.StreamHandler',
                'formatter': 'standard'
            },
            'tracer': {
                'level':'DEBUG',
                'class':'logging.StreamHandler',
                'formatter': 'tracer'
            },
        },
        'loggers': {
            'web_app': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False,
            },
            # 'django.request': {
            #     'handlers': ['mail_admins'],
            #     'level': 'ERROR',
            #     'propagate': True,
            # },
            'django.db': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': False,
            },
            'django': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'TRACER': {
                'handlers': ['tracer'],
                'level': 'DEBUG',
                'propagate': False,
            },
        }
    }
