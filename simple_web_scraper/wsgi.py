"""
WSGI config for simple_web_scraper project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simple_web_scraper.settings")

application = get_wsgi_application()

# see about serving static files with Whitenoise at Herokyu's doc page
# https://devcenter.heroku.com/articles/django-assets
if os.environ.get('WHITENOISE_ENABLED', '').lower() in {'true', '1'}:
    from whitenoise.django import DjangoWhiteNoise
    application = DjangoWhiteNoise(application)

