from .mpr_server import *

DEBUG = True
DEV_VERSION = True

sentry_sdk.init(
    dsn="https://6a33d241537844c5b963cc3c3ba210fa@sentry.acdh-dev.oeaw.ac.at/4",
    integrations=[DjangoIntegration()],
    environment="development"
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
