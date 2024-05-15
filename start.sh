#!/bin/bash
#useradd -M celery
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
python manage.py migrate
python manage.py collectstatic --noinput
#ls /var/solr_new/paas_solr
#python manage.py build_solr_schema --configure-directory /var/solr_new/paas_solr/conf --reload-core default
if [[ -z "${DEVELOP}" ]]; then
    echo "starting gunicorn"
    gunicorn apis.wsgi -b 0.0.0.0:5000 --timeout 120 --workers=3 --threads=3 --worker-connections=1000 --access-logfile - --error-logfile -
fi
