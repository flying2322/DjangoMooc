"""
ASGI config for my_dj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_dj.settings")

application = get_asgi_application()
