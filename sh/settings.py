# Django settings for django_userena project.
import os
###############Email setup##############

DEFAULT_FROM_EMAIL = 'ScribbleHack <do_not_reply@scribblehack.com>'
EMAIL_HOST = 'mail.scribblehack.com'
EMAIL_HOST_USER = 'do_not_reply@scribblehack.com'
EMAIL_HOST_PASSWORD = 'Gnaber500'
EMAIL_PORT = 26

########################################

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-4l38s4%bcm9a34m5xg#jk^#k-t-m(^g6m+dto@os3y$c1-3=5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

MEDIA_ROOT = '/home2/scribbo1/scribblehack/sh/static'

MEDIA_URL = '/static/'

# Application definition

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "/home2/scribbo1/scribblehack/sh/templates/"
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sh.urls'

WSGI_APPLICATION = 'sh.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'scribbo1_sh',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'scribbo1_jc',
        'PASSWORD': 'erdenheim',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
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

STATIC_URL = '/static/'


AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    #'django.contrib.staticfiles',
    'userena',
    'guardian',
    'easy_thumbnails',
    'accounts',
    'django.contrib.admin',
    'widget_tweaks',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

ANONYMOUS_USER_ID = -1
AUTH_PROFILE_MODULE = 'accounts.MyProfile'

LOGIN_REDIRECT_URL = ''
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'