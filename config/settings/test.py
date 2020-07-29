""" Testing settings.
With these settings, tests run faster.
"""

from .base import *  # NOQA
from .base import env

# Base
DEBUG = False
SECRET_KEY = env("DJANGO_SECRET_KEY", default="u&3v29b$ku^f@q#%eq@k13@)lytx+6e+)z4r$92i0+zx6&g)&$")
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# Cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": ""
    }
}

# Passwords
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
