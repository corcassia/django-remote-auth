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

    DATABASE_ROUTERS = ['mysite.db_router.RemoteRouter']
```

And you should add a db route for your remote database, for example:
```python
class RemoteRouter(object):

    def db_for_read(self, model, **hints):
        # ...
        if model._meta.app_label == 'remote_auth':
            return 'remote_auth'
        # ...

    def db_for_write(self, model, **hints):
        # ...
        if model._meta.app_label == 'remote_auth':
            return 'remote_auth'
        # ...
```

