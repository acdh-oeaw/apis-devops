# Generic APIS Devops to ACDH-CH Cluster
This is a centralised APIS repository for deployment of default APIS instances to the ACDH-CH cluster.

## Adding a new instance
For spinning up a new instance you need to:
* Get a new database on Helios (ask an admin to get one)
* Add a new deployment section to `.gitlab-ci.yml`:
    ```
    deploy_PROJECT_SLUG-STAGE:
        <<: *production_template
        environment:
            name: PROJECT_SLUG-STAGE
            url: http://$CI_PROJECT_PATH_SLUG.$KUBE_INGRESS_BASE_DOMAIN
            deployment_tier: production
            ```
    PROJECT_SLUG: short name defining the project (e.g mpr or pmb)
    STAGE: prod (for production) or dev (for development)
* commit the changes to the repo and stop the pipeline execution (pipeline would fail for the new environment). Gitlab automatically added the environment name you used in the `.gitlab-ci.yml` snippet.
* Head over to https://rancher.acdh-dev.oeaw.ac.at and add a new namespace for the instance to a project (prefereable in the [APIS Project](https://rancher.acdh-dev.oeaw.ac.at/p/c-zdbh8:p-d4v6m/ns))
* Add the following variables to Settings-CI/CD-Variables and set the Environment Scope to the newly created environment:
    - KUBE_NAMESPACE: the namespace you just adde`
    - DATABASE_URL: add the information on the database you want to use in the form of `DATABASE_TYPE://USER:PASSWORD@helios.arz.oeaw.ac.at:PORT/DATABASE`
        - DATABASE_TYPE: either postgresql or mysql
        - USER: Database user
        - PASSWORD: Password of the user
        - PORT: 3306 for mysql, 5432 for postgresql
        - DATABASE: Database to use
    - HELM_UPGRADE_EXTRA_ARGS: Extra arguments for the deployment in the form of `--set service.url=EXTERNAL_URL --set-string podLabels.ID=REDMINE_ID --set livenessProbe.initialDelaySeconds=180 --set readinessProbe.initialDelaySeconds=180`
        - EXTERNAL_URL: The URL you want to use for external access (needs to be directed to the cluster by an admin)
        - REDMINE_ID: Every service needs a Redmine ID. If you havent set up a service issue yet, head over to [Redmine](https://redmine.acdh.oeaw.ac.at/), set one up and add the ticker ID here.
    - K8S_SECRET_DJANGO_SETTINGS_MODULE: Path of the Django setting to use in dot notation (e.g. apis.settings.mpr_server). You can either reuse one of the settings already available or add a new one to the repo
    - K8S_SECRET_ALLOWED_HOSTS (optional): If you reuse an existing setting you might want to override the `ALLOWED_HOSTS` with this env variable. E.g. `"localhost,127.0.0.1,mpr.acdh.oeaw.ac.at,mpr.acdh-cluster.arz.oeaw.ac.at"
* [Run the pipeline](https://gitlab.com/acdh-oeaw/apis/apis-devops/-/pipelines/new) manually to deploy the new instance

# Robots.txt Handling

Basic robots.txt template served from the 'robots_template' folder in the root directory

If you whish to serve a custom robots txt:
- create an additional folder in the root directory
- the folder can have any name
- place your custom robots.txt inside this folder
- the file must be named robots.txt
- in your project-settings, change the value of the 'ROBOTS_TXT_FOLDER' variable 
- DONE 


