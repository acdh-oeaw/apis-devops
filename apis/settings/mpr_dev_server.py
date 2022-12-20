from .mpr_server import *

DEBUG = True
DEV_VERSION = True

sentry_sdk.init(
    dsn="https://acd80363d7bb481da8dcbf763e4919e3@o4504360778661888.ingest.sentry.io/4504360893677568",
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

####### ROBOTS.TXT HANDLING #######

# robots.txt file needs to be located in a folder that is registered as a template-dir
# both the end of the url from where the file is served as well as the file itself needs to be named robots.txt
# if you want to add your own robots txt, create a new folder in the root directory and register it here

# replace the path to the folder in which the robots.txt file is to be found here
ROBOTS_TXT_FOLDER = os.path.join(BASE_DIR, "robots_template")

# register above folder as a template-dir
TEMPLATES[0]["DIRS"] += [ROBOTS_TXT_FOLDER,]