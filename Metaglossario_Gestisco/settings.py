"""
Django settings for Metaglossario_Gestisco project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os ###
import django_heroku ###
from decouple import config ###

# per gestire user e password del database postgresql che cambiano ogni 24 ore sugli host
import dj_database_url ###

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# scret_key hidden in env variable files hidden from git
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'import_export',
    'django_filters',
    'app_metaglossario',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware', #zips up static files
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Metaglossario_Gestisco.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Metaglossario_Gestisco.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        
    }
}


database__default_credential_url= config("DATABASE_URL")

# nascondi questa password
# password 1 - .passwords.txt
DATABASES['default']=dj_database_url.config(default=database__default_credential_url)

# #postgres://user:password@host:porta/database_name

#di questo comandi qui sopra DATABASES['default']=dj_database_url.config(default=  
# non c'è bisogno in produzione  
# perchè heroku maneggia questo usando dj database che ho messo sopra con dj_database_url
# ne ho bisogno solo in locale per accedere al database.
# quindi alla fine della produzione devo cancellarlo

# questi sono settings minori
db_from_env=dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

# aggiunta delle funzioni di hashers per user authentication


PASSWORD_HASHERS = [
    
    'django.contrib.auth.hashers.Argon2PasswordHasher',   
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',

    # prova ad installarli uno ad uno, in serie

]

# questi bloccano le password semplici inserite dall'utente
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS':{'min_length':8}
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# linea creata automaticamente da django
STATIC_URL = '/static/'

# Queste tre linee e aggiungo io
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATICSTORAGE = "Whitenoise.storage.CompressedManifestStaticFilesStorage" #zips up static files

django_heroku.settings(locals())  ###

#aggiunto per far funzionare il modulo di importazione csv in admin
IMPORT_EXPORT_USE_TRANSACTIONS = True

# aggiunto per indicare la directory dei files salvati dallìupload degli utenti
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploaded_files')
MEDIA_URL = '/uploaded_files/'

DATA_UPLOAD_MAX_NUMBER_FIELDS = 13000 # higher than the count of fields