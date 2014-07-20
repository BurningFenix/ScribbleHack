#settings/local.py
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "/home/jc/Documents/ScribbleHack/templates")

#INSTALLED_APPS + = ("debug_toolbar", ) 
INTERNAL_IPS = ("127.0.0.1",) 
#MIDDLEWARE_CLASSES + = \ ("debug_toolbar.middleware.DebugToolbarMiddleware", )

