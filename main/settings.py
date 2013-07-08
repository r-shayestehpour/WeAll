# Django settings for weAll project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Arash', 'a.khajelou@gmail.com'),
)

MANAGERS = ADMINS

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'we_all_db',                           # Or path to database file if using sqlite3.
        'USER': 'root',                           # Not used with sqlite3.
        'PASSWORD': 'mysql123',                       # Not used with sqlite3.
        'HOST': 'localhost',                           # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                           # Set to empty string for default. Not used with sqlite3.
    }
}

ALLOWED_HOSTS = ['*']
TLANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
import os
ROOT_DIR = (os.path.join(os.path.dirname(__file__), '..',).replace('\\','/'),)
ROOT = ROOT_DIR[0][:len(ROOT_DIR[0])-8]
print ROOT
MEDIA_ROOT = ROOT_DIR[0]+'/media'
MEDIA_URL = '/media/'
STATIC_ROOT = ROOT_DIR[0]+'/static'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
   ROOT_DIR[0]+'/main',
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'pt8^f#c03_a863niog0fjbrl&amp;cg$-@=%kaqit@#t^bmt34s60z'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages'
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
ROOT_URLCONF = 'main.urls'
WSGI_APPLICATION = 'main.wsgi.application'
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chat',
    'dajaxice',
    'friends',
    # 'django.contrib.admin',
    # 'django.contrib.admindocs',
    'main' ,
    'login',
    'register'
)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
