from .base import *
import os
import dj_database_url
import re

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^mm-24*i-6iecm7c@z9l+7%^ns^4g^z!8=dgffg4ulggr-4=1%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = re.sub(
    r"https?://",
    "",
    os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1,mpr.acdh.oeaw.ac.at,mpr.acdh-cluster.arz.oeaw.ac.at,mpr.acdh-dev.oeaw.ac.at,.acdh-cluster.arz.oeaw.ac.at"),
).split(",")
# You need to allow '10.0.0.0/8' for service health checks.
ALLOWED_CIDR_NETS = ["10.0.0.0/8", "127.0.0.0/8"]

DEV_VERSION = False
APIS_LIST_VIEWS_ALLOWED = True
APIS_DETAIL_VIEWS_ALLOWED = True

DATABASES = {}

DATABASES["default"] = dj_database_url.config(conn_max_age=600)

REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = (
    "rest_framework.permissions.IsAuthenticatedOrReadOnly",
)

CSP_DEFAULT_SRC += ("www.oeaw.ac.at", "mrp.oeaw.ac.at")

APIS_RELATIONS_FILTER_EXCLUDE += ['annotation', 'annotation_set_relation']

REDMINE_ID = "11695"

APIS_BASE_URI = "https://mpr.acdh.oeaw.ac.at/"

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
    dsn="https://acd80363d7bb481da8dcbf763e4919e3@o4504360778661888.ingest.sentry.io/4504360893677568",
    integrations=[DjangoIntegration()],
    environment="production",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
PROJECT_NAME = "mpr"

####### ROBOTS.TXT HANDLING #######

# robots.txt file needs to be located in a folder that is registered as a template-dir
# both the end of the url from where the file is served as well as the file itself needs to be named robots.txt
# if you want to add your own robots txt, create a new folder in the root directory and register it here

# replace the path to the folder in which the robots.txt file is to be found here
ROBOTS_TXT_FOLDER = os.path.join(BASE_DIR, "robots_template")

# register above folder as a template-dir
TEMPLATES[0]["DIRS"] += [ROBOTS_TXT_FOLDER,]