from .base import*

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm11q@hqhdgz=57n3ns0&l%&t71_n5a2w&7!2nv2!se1d1(sg4v'

DATABASES = {
    'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'ecomrest',
                'USER': 'postgres',
                'PASSWORD': '84253675',
                'HOST': '127.0.0.1',
                'PORT': '5432',

    }

}
