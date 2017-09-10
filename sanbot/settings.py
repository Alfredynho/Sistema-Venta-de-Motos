from __future__ import absolute_import, unicode_literals
import os

from os.path import join, dirname
from django.utils.translation import ugettext_lazy as _


PROJECT_PATH = dirname(dirname(dirname(__file__)))
APPS_PATH = join(PROJECT_PATH, "apps")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ["*"]

SECRET_KEY = 'm6c-&_17ki^f4z_2icp^@$yuy$@5u$%fu=4x7857ho=y%-m8lw'

DEBUG = True


# ALLOWED_HOSTS = default=['warpp.xyz']


# ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['warpp.xyz'])


# App django
DJANGO_APPS = (
    # 'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# App de Terceros
THIRD_PARTY_APPS = (
    # Para dar estilos usando bootstrap a los campos de los formularios
    'bootstrap3',
    'django.contrib.humanize',
    # 'easy_pdf',
    'imagekit',
    'compressor',
    'constance',
    'datetimewidget', 
)

# Apps Locales
LOCAL_APPS = (
    # apps locales
    'apps.inicio',
    'apps.cuenta',
    'apps.empleado',
    'apps.producto',
    'apps.cliente',
    'apps.venta',
    'apps.proveedor',
    'apps.messenger',
    'apps.repuesto',
    'apps.propaganda',
    'apps.reparacion',
    'apps.users',
)

AUTH_USER_MODEL = 'users.User'


INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'sanbot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,  'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'sanbot.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'USMBOTS'),
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'usm_app',
        'USER': 'usm_user',
        'PASSWORD': 'XXXYYYZZZ',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# # CACHE CONFIGURATION
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#     }
# }

# CONSTANCE_REDIS_CONNECTION = 'redis://username:password@localhost:6379/0'
CONSTANCE_CONFIG = {
    'PAGE_ACCESS_TOKEN': ("CAMBIAR ESTE TOKEN", _("Este token es generado entre la aplicación y la página de facebook")),
    'VALIDATION_CODE': ("AGREGAR UN CÓDIGO", _("Este Código de validación servira para verificar un webhook en facebook")),
    'CONTINUOS_MENU': (False, _("Activa o desactiva el Menu continuo del ChatBot")),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'Messenger': ('PAGE_ACCESS_TOKEN', 'VALIDATION_CODE', 'CONTINUOS_MENU'),
}

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

LANGUAGE_CODE = 'es-BO'

TIME_ZONE = 'America/La_Paz'


SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

usel10n = True

STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)



# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
MEDIA_ROOT = join(PROJECT_PATH, 'public/media/')
MEDIA_URL = '/media/'

# PLATFORM SETTINGS
# ------------------------------------------------------------------------------
PROJECT_NAME = "MBOT"
PROJECT_AUTHOR = "GITBO"
PROJECT_DOMAIN = "http://gitbo.xyz"

