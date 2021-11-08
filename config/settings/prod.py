from .base import *

ALLOWED_HOSTS = ['3.37.252.11', 'finds.or.kr']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bbs',
        'USER': 'dbmasteruser',
        'PASSWORD': 'p-}6L_cFZud<6;f=|QDnmhD1h]%Shn>G',
        'HOST': 'ls-2ae92affc0cdb022150f0c6dbde4fda896d79f52.cvr2ypsq2s8v.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}