INSTALLED_APPS = [
    ...
    'django_htmx',
    'debug_toolbar',
    'posts',
    ...
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    ...
]

INTERNAL_IPS = ['127.0.0.1']
