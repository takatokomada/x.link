"""
WSGI config for com project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
import sys
import os
from django.core.wsgi import get_wsgi_application
SECRET_KEY = os.environ.get('django-insecure-4nar-6*z84n7vb%hv_c=3xc6!n@i98sxgf_u82q#%bjr*yw3q0')
sys.path.append('/Users/komadatakahito/Sites/com')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'com.settings')
application = get_wsgi_application()
