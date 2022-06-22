import dj_database_url

from .base import *
import sys


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

APIS_BASE_URI = "https://apis.acdh.oeaw.ac.at/"

ALLOWED_HOSTS = []

SECRET_KEY = 'd3j@454545()(/)@zlck/6dsaf*#sdfsaf*#sadflj/6dsfk-11$)d6ixcvjsdfsdf&-u35#ayi'
DEBUG = True
DEV_VERSION = False

INSTALLED_APPS += ['gm2m', 'apis_highlighter']

DATABASES = {}

DATABASES['default'] = dj_database_url.config(conn_max_age=600)


LANGUAGE_CODE = "de"

APIS_RELATIONS_FILTER_EXCLUDE += ['annotation', 'annotation_set_relation']


####### ROBOTS.TXT HANDLING #######

# robots.txt file needs to be located in a folder that is registered as a template-dir
# both the end of the url from where the file is served as well as the file itself needs to be named robots.txt
# if you want to add your own robots txt, create a new folder in the root directory and register it here

# replace the path to the folder in which the robots.txt file is to be found here
ROBOTS_TXT_FOLDER = os.path.join(BASE_DIR, "robots_template")

# register above folder as a template-dir
TEMPLATES[0]["DIRS"] += [ROBOTS_TXT_FOLDER,]