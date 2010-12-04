import os
import platform

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))

if PROJECT_PATH.startswith('/var/www/ideas/'): #PRODUCTION
    from prod import *
else:
    from local import *

