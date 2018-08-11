from .base import *

import dj_database_url


SECRET_KEY = os.environ['SECRET_KEY']

WSGI_APPLICATION = 'wsgi.application'

DATABASE_URL = os.environ['DATABASE_URL']
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL),
}
