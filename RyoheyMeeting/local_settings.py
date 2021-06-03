import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3%=7fx1ibgdh!!oakp1!3lrk^-kb9#aason4#^4^+kgc!eh#ud'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '217334756916-lr2727rv947uc71rd20r1onomnmqks29.apps.googleusercontent.com'  #Paste CLient Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '36nTsCPfyNUC6D2Esq1KoWxL' #Paste Secret Key
