from .base import *
import re
import dj_database_url
import os


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "^mm-24*i-6iecm7c@z9l+7%^ns^4g^z!8=dgffg4ulggr-4=1%"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# REDMINE_ID = "14590"
APIS_LIST_VIEWS_ALLOWED = False
APIS_DETAIL_VIEWS_ALLOWED = False
FEATURED_COLLECTION_NAME = "FEATURED"
# MAIN_TEXT_NAME = "ÖBL Haupttext"
#BIRTH_REL_NAME = [64, 152, 3090]
#DEATH_REL_NAME = [153, 3054, 3091]
APIS_BASE_URI = "https://viecpro.acdh.oeaw.ac.at/"
# APIS_OEBL_BIO_COLLECTION = "ÖBL Biographie"

APIS_SKOSMOS = {
    "url": os.environ.get("APIS_SKOSMOS", "https://vocabs.acdh-dev.oeaw.ac.at"),
    "vocabs-name": os.environ.get("APIS_SKOSMOS_THESAURUS", "apisthesaurus"),
    "description": "Thesaurus of the APIS project. Used to type entities and relations.",
}

ALLOWED_HOSTS = re.sub(
    r"https?://",
    "",
    os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1,viecpro-dev.acdh-dev.oeaw.ac.at,.acdh-cluster.arz.oeaw.ac.at"),
).split(",")
# You need to allow '10.0.0.0/8' for service health checks.
ALLOWED_CIDR_NETS = ["10.0.0.0/8", "127.0.0.0/8"]

CSP_DEFAULT_SRC = CSP_DEFAULT_SRC + ("sharonchoong.github.io", "github.com/devongovett")

SECRET_KEY = (
    "d3j@454545()(/)@zlck/6dsaf*#sdfsaf*#sadflj/6dsfk-11$)d6ixcvjsdfsdf&-u35#ayi"
)
DEBUG = True
DEV_VERSION = False

SPECTACULAR_SETTINGS["COMPONENT_SPLIT_REQUEST"] = True
SPECTACULAR_SETTINGS["COMPONENT_NO_READ_ONLY_REQUIRED"] = True


INSTALLED_APPS += ["viecpro_vis", "dubletten_tool"]

DATABASES = {}

DATABASES["default"] = dj_database_url.config(conn_max_age=600)

#MAIN_TEXT_NAME = "ÖBL Haupttext"

LANGUAGE_CODE = "de"


APIS_RELATIONS_FILTER_EXCLUDE = [
    "*uri*",
    "*tempentityclass*",
    "user",
    "*__id",
    "*source*",
    "label",
    "*temp_entity*",
    "*collection*",
    "*published*",
    "*_set",
    "*_set__*",
    "_ptr",
    "baseclass",
    "*id",
    "*written*",
    #"relation_type__*",
    "*__text*",
    "text*",
    "*annotation_set_relation*",
    "*start_start_date*",
    "*end_end_date*",
    "*start_end_date*",
    "*end_start_date*",
    "*label*",
    "*review*",
    "*__status",
    "*__references",
    "*__notes",
]





# APIS_COMPONENTS = ['deep learning']

# APIS_BLAZEGRAPH = ('https://blazegraph.herkules.arz.oeaw.ac.at/metaphactory-play/sparql', 'metaphactory-play', 'KQCsD24treDY')


APIS_RELATIONS_FILTER_EXCLUDE += ["annotation", "annotation_set_relation"]

VIECPRO_VIS_BASE_URI = "https://viecpro-dev.acdh-dev.oeaw.ac.at/"


import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://875005d9fd8c41878a5d9a309a17403c@sentry.acdh-dev.oeaw.ac.at/5",
    integrations=[DjangoIntegration()],
    environment="development",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
