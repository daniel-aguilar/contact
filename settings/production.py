import os

BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['contact-daniel.herokuapp.com']

INSTALLED_APPS = [
    'contact',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    },
    {
        'NAME': 'plaintext',
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'autoescape': False,
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_TZ = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'application.log',
            'formatter': 'default',
        }
    },
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        }
    },
    'loggers': {
        'contact': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    },
}

SECURE_SSL_REDIRECT = True

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_RECIPIENT = os.getenv('EMAIL_RECIPIENT')

RECAPTCHA_SECRET_KEY = os.getenv('RECAPTCHA_SECRET_KEY')

HOMEPAGE_URL = os.getenv('HOMEPAGE_URL')
CONTACT_URL = os.getenv('CONTACT_URL')
