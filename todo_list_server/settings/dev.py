import os

from todo_list_server.settings.base import *

DEBUG = True

LOGGING_DEFAULT_LEVEL = 'ERROR'
LOGGING_APPS_LEVEL = 'DEBUG'
LOGGING_CONSOLE_HANDLER = 'console'
LOGGING_FILE_HANDLER = 'file_default'
LOGGING_DEFAULT_HANDLERS = [LOGGING_CONSOLE_HANDLER, LOGGING_FILE_HANDLER]
LOGGING_DEFAULT_FILENAME = os.path.join(LOGS_DIR, 'todolist.log')

# Logging config
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s %(levelname)s] (%(module)s): %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        LOGGING_CONSOLE_HANDLER: {
            'level': LOGGING_DEFAULT_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'filters': ['require_debug_true'],
        },
        LOGGING_FILE_HANDLER: {
            'level': LOGGING_DEFAULT_LEVEL,
            'class': 'logging.FileHandler',
            'filename': LOGGING_DEFAULT_FILENAME,
            'formatter': 'verbose',
            'filters': [],
        },
    },
    'loggers': {
        'django': {
            'handlers': LOGGING_DEFAULT_HANDLERS,
            'level': LOGGING_DEFAULT_LEVEL,
            'propagate': False,
        },
        'django.request': {
            'handlers': LOGGING_DEFAULT_HANDLERS,
            'level': LOGGING_DEFAULT_LEVEL,
            'propagate': False,
        },
        'todolist': {
            'handlers': LOGGING_DEFAULT_HANDLERS,
            'level': LOGGING_APPS_LEVEL,
            'propagate': False,
        },
    }
}
