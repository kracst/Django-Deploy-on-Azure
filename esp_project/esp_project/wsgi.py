
import os

from django.core.wsgi import get_wsgi_application

settings_module = 'esp_project.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'esp_project.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
