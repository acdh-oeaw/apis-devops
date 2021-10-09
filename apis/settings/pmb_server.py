from .base import *
import os
import dj_database_url
import re

SECRET_KEY = '^mm-24*i-6iecm7c@0biscH4/7z9l+7%^ns^4g^z!8=dgffg4ulggr-4=1%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DEV_VERSION = False
APIS_LIST_VIEWS_ALLOWED = True
APIS_DETAIL_VIEWS_ALLOWED = True
CUSTOM_LOGO_IMG = "https://shared.acdh.oeaw.ac.at/apis/pmb/project-logo.svg"
REDMINE_ID = "13424"
LANGUAGE_CODE = "de"

REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = (
    "rest_framework.permissions.IsAuthenticatedOrReadOnly",
)

PROJECT_NAME = "pmb"

APIS_BASE_URI = "https://pmb.acdh.oeaw.ac.at/"

REDMINE_ID = "13424"
APIS_RELATIONS_FILTER_EXCLUDE += ['annotation', 'annotation_set_relation']

DATABASES = {}

DATABASES["default"] = dj_database_url.config(conn_max_age=600)

CSP_DEFAULT_SRC = ("'self'", "'unsafe-inline'", 'cdnjs.cloudflare.com', 'cdn.jsdelivr.net', 'fonts.googleapis.com', 'ajax.googleapis.com', 'cdn.rawgit.com', "*.acdh.oeaw.ac.at", "unpkg.com", "fonts.gstatic.com", "cdn.datatables.net", "code.highcharts.com", "*.acdh-dev.oeaw.ac.at", "*.acdh.oeaw.ac.at")
CSP_FRAME_SRC = ('sennierer.github.io',)

ALLOWED_HOSTS = re.sub(
    r"https?://",
    "",
    os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1,pmb.acdh.oeaw.ac.at,.acdh-cluster.arz.oeaw.ac.at,pmb.acdh-dev.oeaw.ac.at,pmbdev.acdh-cluster.arz.oeaw.ac.at"),
).split(",")
# You need to allow '10.0.0.0/8' for service health checks.
ALLOWED_CIDR_NETS = ["10.0.0.0/8", "127.0.0.0/8"]

APIS_SKOSMOS = {
    'url': os.environ.get('APIS_SKOSMOS', 'https://vocabs.acdh-dev.oeaw.ac.at'),
    'vocabs-name': os.environ.get('APIS_SKOSMOS_THESAURUS', 'pmbthesaurus'),
    'description': 'Thesaurus of the PMB project. Used to type entities and relations.'
}

BIRTH_REL = [88, ]
DEATH_REL = [89, ]
PL_A_PART_OF = [1106, 1136]
PL_B_LOCATED_IN = [971, ]

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://e6df764cf0764433afdf9ea28242ad19@sentry.io/1882744",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

