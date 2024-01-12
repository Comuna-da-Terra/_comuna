"""
Django settings for API project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import os
import dotenv
dotenv.load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '192.168.1.103', 'localhost']


# Application definition


DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
THIRD_PARTY_APPS = [
    "rest_framework",
    'corsheaders',
]
PROJECT_APPS = [
    "accounts",
    "products",
    "orders",
    "adresses",
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "_core.urls"
CORS_ALLOW_ALL_ORIGINS = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "_core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        # "ENGINE": "django.db.backends.sqlite3",
        # "NAME": BASE_DIR / "db.sqlite3",
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": "127.0.0.1",
        "PORT": 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME': timedelta(days=1),  
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    'UPDATE_LAST_LOGIN': True,
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}
# REST_FRAMEWORK = {
#     "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
#     "PAGE_SIZE": 5,
# }

# SIMPLE_JWT = {
#     #Um objeto datetime.timedelta que especifica por quanto tempo os tokens de acesso são válidos.
#     'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
#     #Um objeto datetime.timedelta que especifica por quanto tempo os tokens de atualização são válidos.
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=7),

#     #O algoritmo da biblioteca PyJWT que será usado para realizar operações de assinatura/verificação em tokens.
#     'ALGORITHM': 'HS256',
#     #A chave de assinatura que é usada para assinar o conteúdo dos tokens gerados.
#     'SIGNING_KEY': SECRET_KEY,

#     #Os tipos de cabeçalho de autorização que serão aceitos para visualizações que exigem autenticação.
#     'AUTH_HEADER_TYPES': ('Bearer',),
#     #O nome do cabeçalho de autorização a ser usado para autenticação.
#     'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',

#     #Uma tupla contendo as classes que especificam os tipos de token que têm permissão para provar a autenticação.
#     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',)
# }

CSRF_TRUSTED_ORIGINS = []

AUTH_USER_MODEL = "accounts.User"
