# vercel_app.py
import os
import sys

# Add the project directory to the sys.path
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farmproject.settings')

# Import and get the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Export the WSGI application as app (Vercel requires this name)
app = application