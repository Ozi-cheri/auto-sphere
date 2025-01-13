import dotenv
import os

dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))


"""
WSGI config for autosphere project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autosphere.settings')

application = get_wsgi_application()
