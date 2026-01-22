from pathlib import Path
import os
import tempfile
import atexit
import pymysql
pymysql.install_as_MySQLdb()

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.getenv('SECRET_KEY')


DEBUG = os.getenv('DEBUG', 'False') == 'True'

EQ_MODEL_NAME = os.getenv('EQ_MODEL_NAME', 'sreenathsree1578/Bert_fine_tuned_eq')
EQ_FALLBACK_MODEL_NAME = os.getenv('EQ_FALLBACK_MODEL_NAME', 'distilbert-base-uncased')

ALLOWED_HOSTS = ['test-eq.onrender.com']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'assessment',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

ROOT_URLCONF = 'eq_assessment.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'eq_assessment.wsgi.application'


# Database
# Handle SSL Certificate from environment
ssl_ca_path = os.getenv('DB_SSL_CA')
ssl_ca_content = os.getenv('DB_SSL_CA_CONTENT')

if ssl_ca_content:
    # Create a temporary file to store the CA certificate
    tf = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.pem', encoding='utf-8')
    # Convert escaped newlines back to actual newlines
    tf.write(ssl_ca_content.replace('\\n', '\n'))
    tf.close()
    ssl_ca_path = tf.name
    
    # Ensure cleanup on exit
    def cleanup_ssl_cert():
        try:
            if os.path.exists(ssl_ca_path):
                os.unlink(ssl_ca_path)
        except Exception:
            pass
    atexit.register(cleanup_ssl_cert)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
        'OPTIONS': {
            'ssl': {
                'ssl-mode': 'REQUIRED',
                'ca': ssl_ca_path,
            },
        },
    }
}



# Password validation

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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'assessment': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
