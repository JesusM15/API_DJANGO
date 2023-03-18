"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-uz9&kr)h-@un%c_*l)f(7@b%6!l^$ovzr=vs^x$w^=w)s^7e81'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#aplicaciones predeterminadas de Django
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

#aplicaciones descargadas
EXTRA_APPS = [
    'rest_framework.authtoken',
    'rest_framework',
    'drf_spectacular',
    'simple_history',
]

# aplicaciones creadas 
CREATED_APPS = [
    'api',
    'users'
]

#aplicaciones utilizadas en todo el proyecto(predeterminadas + creadas + extensiones)
INSTALLED_APPS = DJANGO_APPS + CREATED_APPS + EXTRA_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

#conexion a la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Tareasapi2',
        'USER': 'postgres',
        'PASSWORD': 'h12345z_je',
        'HOST': 'localhost',
        'PORT': 5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

AUTH_USER_MODEL = 'users.User'

# Django DRF configuraciones
REST_FRAMEWORK = {
    #metodo de autenticacion para todas las peticiones
    'DEFAULT_AUTHENTICATION_CLASSES': (
        #es por medio de una clase de simpleJWT
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    #permisos que definiremos (se validaran al hacer una consulta en un endpoint)
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    #spectacular generara el esquema
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# Django-spectacular configuraciones
SPECTACULAR_SETTINGS = {
    'TITLE': 'TasksAPI',
    'DESCRIPTION': 'Prueba tecnica',
    'VERSION': '1.0.0',
    'CONTACT': {
        'name': 'Jesus M',
        'email': 'guerrajesusm72@gmail.com',
    },
    'SWAGGER_UI_SETTINGS': {
        #permite que al poner un Token se guarda en sesion y este disponible para no hacer peticiones para token cada vez que se recarga la pagina 
      'persistAuthorization': True,  
    },
}

#simple JWT configuraciones
SIMPLE_JWT = {
    #algoritmo de encriptacion
    'ALGORITHM': 'HS256',
    'AUTH_HEADER_TYPES': ('Bearer', ),
    #como buscar al usuario
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    #clases para definir como se comportara el token
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    #tipo token lo que se validara
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',
}


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'