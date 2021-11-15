"""
Quick-start development settings - unsuitable for production
See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / "apps" / "template"
STATIC_DIR = BASE_DIR / "assets" / "static_cdn"
MEDIA_DIR = BASE_DIR / "assets" / "media_cdn"
SECRET_KEY_FILE = BASE_DIR / "assets" / "secret_key.txt"

while not SECRET_KEY_FILE.exists():
    with open(SECRET_KEY_FILE, "w") as f:
        from django.core.management.utils import get_random_secret_key
        f.write(get_random_secret_key())

with open(SECRET_KEY_FILE, "r") as f:
    SECRET_KEY = f.read().strip()

DEBUG = int(os.environ.get("DEBUG")) == 1
ALLOWED_HOSTS = list(os.environ.get("ALLOWED_HOSTS").split(","))

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # THIRD_PARTY_APPS
    "corsheaders",
    "rest_framework",
    # LOCAL_APPS
    "apps.utils",
    "apps.data_access",
    "apps.api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # django-cors-headers
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.context_processors.admin_site_header",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator", },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = STATIC_DIR
MEDIA_URL = "/media/"
MEDIA_ROOT = MEDIA_DIR
STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ADMIN_SITE_HEADER = "Administration"
AUTH_USER_MODEL = "data_access.User"
LOGIN_URL = "login"
LOGOUT_REDIRECT_URL = "login"
LOGIN_REDIRECT_URL = "/admin/"


REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer", ],
    "DEFAULT_PARSER_CLASSES": ["rest_framework.parsers.JSONParser", ],
}

# CORS Config
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]
