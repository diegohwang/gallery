import os
import sys
sys.path.append("/home/huangjm/study/mydjango")
sys.path.append("/home/huangjm/study/mydjango/gallery")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gallery.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()