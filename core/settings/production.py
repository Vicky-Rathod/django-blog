from .base import *
import dj_database_url

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['https://mohammadanarul.herokuapp.com/', '*']

# database management
DATABASES = {'default': dj_database_url.config()}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('NAME'),
#         'USER': config('USER'),
#         'PASSWORD': config('PASSWORD'),
#         'HOST': config('HOST'),
#         'PORT': config('PORT'),
#     }
# }

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())

# whitenoise collectstatic
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = 'ican4654@gmail.com'
EMAIL_HOST_PASSWORD = "MD367075bd "
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = "ican4654@gmail.com"