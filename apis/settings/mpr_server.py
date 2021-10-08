from .base import *
import os
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^mm-24*i-6iecm7c@z9l+7%^ns^4g^z!8=dgffg4ulggr-4=1%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['mpr.acdh.oeaw.ac.at', 'mpr.acdh-cluster.arz.oeaw.ac.at', '0.0.0.0', 'localhost']

DEV_VERSION = False
APIS_LIST_VIEWS_ALLOWED = True
APIS_DETAIL_VIEWS_ALLOWED = True

INSTALLED_APPS += ['corsheaders']

DATABASES = {}

DATABASES["default"] = dj_database_url.config(conn_max_age=600)

CSP_DEFAULT_SRC = ("'self'", "'unsafe-inline'", 'cdnjs.cloudflare.com', 'cdn.jsdelivr.net', 'fonts.googleapis.com', 'cdn.rawgit.com', "*.acdh.oeaw.ac.at", "unpkg.com", "fonts.gstatic.com", "cdn.datatables.net", "code.highcharts.com", "*.acdh-dev.oeaw.ac.at", "*.acdh.oeaw.ac.at")
CSP_FRAME_SRC = ('sennierer.github.io',)

REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = (
    "rest_framework.permissions.IsAuthenticatedOrReadOnly",
)

CSRF_TRUSTED_ORIGINS = ['mpr.acdh.oeaw.ac.at']

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
    dsn="https://5e98062bebfc4894a0596383f9ad762b@sentry.io/1761169",
    integrations=[DjangoIntegration()]
)

PROJECT_NAME = "mpr"

