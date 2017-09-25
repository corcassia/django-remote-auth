Django remote auth
==================

Provide multiple Django Auth support to a project


Install 
-------

```
pip install remote_auth
```


Quick Start Guide
=================

Add `remote_auth` to your `settings.py`

```python

    INSTALLED_APPS = [
        '...',
        'remote_auth',
        '...'
    ]

    MIDDLEWARE = [
        '...',
        'remote_auth.middleware.SessionMiddleware',
        '...'
    ]

    DATABASES = {
        '...',

        'remote_auth': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'REMOTE_DB',
            'USER': 'REMOTE_USER',
            'PASSWORD': 'REMOTE_PASSWORD',
            'HOST': 'REMOTE_HOST',
            'PORT': 'REMOTE_PORT',
        },

        '...'
    }

    AUTHENTICATION_BACKENDS = [
        'remote_auth.backends.CustomModelBackend',
    ]
```
