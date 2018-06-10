import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['contact-daniel.herokuapp.com']

INSTALLED_APPS = [
    'contact',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'interaction.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'autoescape': False,
        },
    },
]

WSGI_APPLICATION = 'interaction.wsgi.application'

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
        'core': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
        'contact': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    },
}

SECURE_SSL_REDIRECT = True

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_TO_ADDRESS = os.getenv('EMAIL_TO_ADDRESS')

RECAPTCHA_SECRET = os.getenv('RECAPTCHA_SECRET')

CONTACT_URL = os.getenv('CONTACT_URL')
THANKS_URL = os.getenv('THANKS_URL')
ERROR_URL = os.getenv('ERROR_URL')
