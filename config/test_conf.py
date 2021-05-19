from .settings import *


DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'action',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '144.34.188.213',
        'PORT': 5433
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:password@144.34.188.213:65431/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "ip": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:password@144.34.188.213:65431/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:password@144.34.188.213:65431/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}
