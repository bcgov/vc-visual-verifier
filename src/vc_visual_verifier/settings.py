"""
Django settings for vc_visual_verifier project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os


def parse_bool(val):
    return val and val != "0" and str(val).lower() != "false"


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    # safe value used for development when DJANGO_SECRET_KEY might not be set
    "@ml^(k%**i84a2#m6em1^)rt-%chwas3z#w0sz=q3w0ng8zm77",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = parse_bool(os.getenv("DJANGO_DEBUG", "False"))

ALLOWED_HOSTS = ["*"]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "oidc_rp",
    "vc_visual_verifier",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "oidc_rp.middleware.OIDCRefreshIDTokenMiddleware",
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "oidc_rp.backends.OIDCAuthBackend",
)

AUTH_USER_MODEL = "vc_visual_verifier.User"

ROOT_URLCONF = "vc_visual_verifier.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "vc_visual_verifier/templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "oidc_rp.context_processors.oidc",
            ],
        },
    },
]

WSGI_APPLICATION = "vc_visual_verifier.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"

if DEBUG:
    # serve static files from development server
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
else:
    # serve static files using production webserver
    STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Settings for django-oidc-rp
OIDC_RP_PROVIDER_ENDPOINT = os.getenv("OIDC_RP_PROVIDER_ENDPOINT")
OIDC_RP_PROVIDER_AUTHORIZATION_ENDPOINT = (
    f"{OIDC_RP_PROVIDER_ENDPOINT}/vc/connect/authorize"
)
OIDC_RP_PROVIDER_TOKEN_ENDPOINT = f"{OIDC_RP_PROVIDER_ENDPOINT}/vc/connect/token"
OIDC_RP_PROVIDER_JWKS_ENDPOINT = (
    f"{OIDC_RP_PROVIDER_ENDPOINT}/.well-known/openid-configuration/jwks"
)
OIDC_RP_PROVIDER_USERINFO_ENDPOINT = f"{OIDC_RP_PROVIDER_ENDPOINT}/vc/connect/userinfo"
OIDC_RP_CLIENT_ID = os.getenv("OIDC_RP_CLIENT_ID")
OIDC_RP_CLIENT_SECRET = os.getenv("OIDC_RP_CLIENT_SECRET")
OIDC_RP_PROVIDER_SIGNATURE_ALG = "RS256"
OIDC_RP_SCOPES = os.getenv("OIDC_RP_SCOPES", "openid profile vc_authn")
OIDC_RP_ID_TOKEN_INCLUDE_USERINFO = True

# vc-authn proof-configuration
VC_AUTHN_PRES_REQ_CONF_ID = os.getenv("VC_AUTHN_PRES_REQ_CONF_ID")

# Claims to be checked in the UI
OIDC_CLAIMS_REQUIRED = os.getenv("OIDC_CLAIMS_REQUIRED")

# VC verifier name
VERIFIER_NAME = os.getenv("VERIFIER_NAME", "VC Visual Verifier")
