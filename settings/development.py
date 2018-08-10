from .base import *

import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

DATABASE_URL = os.environ['DATABASE_URL']
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL),
}

DATABASES['default']['CONN_MAX_AGE'] = None

# djangosecure settings
SECURE_FRAME_DENY = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')