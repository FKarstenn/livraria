import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'rest_framework',
    'corsheaders',
    "rest_framework_simplejwt",
    "uploader",
    "drf_spectacular",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'livraria.urls'

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

WSGI_APPLICATION = 'livraria.wsgi.application'




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

REST_FRAMEWORK = {
         "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
         "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissions",
         ],
         "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
         )
    
}

AUTH_USER_MODEL = "core.Usuario"

MEDIA_URL = "http://localhost:8000/media/"
MEDIA_ENDPOINT = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
FILE_UPLOAD_PERMISSIONS = 0o640



SPECTACULAR_SETTINGS = {
    "TITLE": "Livraria API",
    "DESCRIPTION": "API para gerenciamento de livraria, incluindo endpoints e documentação.",
    "VERSION": "1.0.0",
}


env = environ.Env()
environ.Env.read_env((os.path.join(BASE_DIR, '.env')))

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(',')
DATABASES = {'default': env.db()}