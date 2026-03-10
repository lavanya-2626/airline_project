"""Development settings — inherits base, enables debug tools."""
from .base import *

DEBUG = True

# In dev, also allow SQLite fallback if MongoDB URI not set
if not MONGODB_URI:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Relax CSRF for local dev
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]
