"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""
# # This file is for asynchronous tasks

import os                    # Imports built-in os module, outputs the module namespace object (E.g., <module 'os' from '...'>)

from django.core.wsgi import get_wsgi_application                    # Imports handler loader function, outputs a callable generator function (E.g., <function get_wsgi_application at 0x...>)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')                    # Configures environment key with 'core.settings' value, outputs string (E.g., 'core.settings')

application = get_wsgi_application()                    # Invokes loader to generate WSGI application, outputs/assigns handler instance (E.g., application: <django.core.handlers.wsgi.WSGIHandler object at 0x...>)
