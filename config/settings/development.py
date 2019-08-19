from .base import *

INSTALLED_APPS.append('django_extensions')

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

DEBUG = True

###########################################################################################################

#                                        template config in setting

###########################################################################################################



TEMPLATES_DIRS = os.path.join(BASE_DIR, 'templates')



TEMPLATES[0]['DIRS'].append(TEMPLATES_DIRS)

###########################################################################################################
#            static file set up
###########################################################################################################

STATIC_DIR = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

STATICFILES_DIRS = [
    STATIC_DIR,
]


MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


###########################################################################################################

# debug toolbar

###########################################################################################################



INSTALLED_APPS.append('debug_toolbar')




MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')



DEBUG_TOOLBAR_PANELS = [

'debug_toolbar.panels.versions.VersionsPanel',

'debug_toolbar.panels.timer.TimerPanel',

'debug_toolbar.panels.settings.SettingsPanel',

'debug_toolbar.panels.headers.HeadersPanel',

'debug_toolbar.panels.request.RequestPanel',

'debug_toolbar.panels.sql.SQLPanel',

'debug_toolbar.panels.staticfiles.StaticFilesPanel',

'debug_toolbar.panels.templates.TemplatesPanel',

'debug_toolbar.panels.cache.CachePanel',

'debug_toolbar.panels.signals.SignalsPanel',

'debug_toolbar.panels.logging.LoggingPanel',

'debug_toolbar.panels.redirects.RedirectsPanel',

]



DEBUG_TOOLBAR_CONFIG = {

'INTERCEPT_REDIRECTS': False,

}



INTERNAL_IPS = ['127.0.0.1']


###########################################################################################################

# Crispy form config

###########################################################################################################



INSTALLED_APPS.append('crispy_forms')

CRISPY_TEMPLATE_PACK = 'bootstrap4'
