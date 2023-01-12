from .base import *
import os
import dj_database_url
import re

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = re.sub(
    r"https?://",
    "",
    os.environ.get("ALLOWED_HOSTS",
"localhost,127.0.0.1,acdh21.acdh-cluster.arz.oeaw.ac.at,acdh21.acdh-dev.oeaw.ac.at,.acdh-cluster.arz.oeaw.ac.at"),
).split(",")
# You need to allow '10.0.0.0/8' for service health checks.
ALLOWED_CIDR_NETS = ["10.0.0.0/8", "127.0.0.0/8"]

DEV_VERSION = False
APIS_LIST_VIEWS_ALLOWED = False
APIS_DETAIL_VIEWS_ALLOWED = False

DATABASES = {}

DATABASES["default"] = dj_database_url.config(conn_max_age=600)

CSP_DEFAULT_SRC = ("'self'", "'unsafe-inline'", 'cdnjs.cloudflare.com', 'cdn.jsdelivr.net', 'ajax.googleapis.com', 'fonts.googleapis.com', 'cdn.rawgit.com', "*.acdh.oeaw.ac.at", "unpkg.com", "fonts.gstatic.com", "cdn.datatables.net", "code.highcharts.com", "*.acdh-dev.oeaw.ac.at", "*.acdh.oeaw.ac.at", "*.oeaw.ac.at")
CSP_FRAME_SRC = ('sennierer.github.io',)

REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = (
    "rest_framework.permissions.IsAuthenticated",
)


APIS_RELATIONS_FILTER_EXCLUDE += ['annotation', 'annotation_set_relation']


APIS_BASE_URI = "https://acdh21.acdh-dev.oeaw.ac.at/"

APIS_SKOSMOS = {
    'url': os.environ.get('APIS_SKOSMOS', 'https://vocabs.acdh-dev.oeaw.ac.at'),
    'vocabs-name': os.environ.get('APIS_SKOSMOS_THESAURUS', 'mprthesaurus'),
    'description': 'Thesaurus of the MPR project. Used to type entities and relations.'
}


APIS_BLAZEGRAPH = (
    os.environ.get('APIS_TRIPLESTORE', 'https://triplestore.acdh-dev.oeaw.ac.at/omnipot/sparql'),
    os.environ.get('APIS_TRIPLESTORE_USERNAME', ''),
    os.environ.get('APIS_TRIPLESTORE_PASSWORD', ''))

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://5e98062bebfc4894a0596383f9ad762b@sentry.io/1761169",
    integrations=[DjangoIntegration()]
)

PROJECT_NAME = "acdh21"


####### ROBOTS.TXT HANDLING #######

# robots.txt file needs to be located in a folder that is registered as a template-dir
# both the end of the url from where the file is served as well as the file itself needs to be named robots.txt
# if you want to add your own robots txt, create a new folder in the root directory and register it here

# replace the path to the folder in which the robots.txt file is to be found here
ROBOTS_TXT_FOLDER = os.path.join(BASE_DIR, "robots_template")

# register above folder as a template-dir
TEMPLATES[0]["DIRS"] += [ROBOTS_TXT_FOLDER,]
