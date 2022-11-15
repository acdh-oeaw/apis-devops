import os
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView


from apis_core.apis_entities.api_views import GetEntityGeneric

if "theme" in settings.INSTALLED_APPS:
    urlpatterns = [
        url(r"^apis/", include("apis_core.urls", namespace="apis")),
        url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
        path(
            r"entity/<int:pk>/", GetEntityGeneric.as_view(), name="GetEntityGenericRoot"
        ),
        url(r"^", include("theme.urls", namespace="theme")),
        url(r"^admin/", admin.site.urls),
        url(r"^info/", include("infos.urls", namespace="info")),
        url(r"^webpage/", include("webpage.urls", namespace="webpage")),
    ]
if "paas_theme" in settings.INSTALLED_APPS:
    urlpatterns = [
        url(r"^apis/", include("apis_core.urls", namespace="apis")),
        url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
        path(
            r"entity/<int:pk>/", GetEntityGeneric.as_view(), name="GetEntityGenericRoot"
        ),
        url(r"^", include("paas_theme.urls", namespace="theme")),
        url(r"^admin/", admin.site.urls),
        url(r"^info/", include("infos.urls", namespace="info")),
        url(r"^webpage/", include("webpage.urls", namespace="webpage")),
    ]
else:
    urlpatterns = [
        url(r"^apis/", include("apis_core.urls", namespace="apis")),
        url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
        path(
            r"entity/<int:pk>/", GetEntityGeneric.as_view(), name="GetEntityGenericRoot"
        ),
        url(r"^admin/", admin.site.urls),
        url(r"^info/", include("infos.urls", namespace="info")),
        url(r"^", include("webpage.urls", namespace="webpage")),
    ]


if 'viecpro_vis' in settings.INSTALLED_APPS:
    urlpatterns.insert(0, url(r'^visualisations/', include("viecpro_vis.urls", namespace="viecpro_vis"))
    )

if 'apis_import_project' in settings.INSTALLED_APPS:
    urlpatterns = urlpatterns + [
         url(r'^apis_import_project/', include("apis_import_project.urls", namespace="apis_import_project"))]

if 'dubletten_tool' in settings.INSTALLED_APPS:
    urlpatterns = urlpatterns + [
        url(r'^dubletten/', include("dubletten_tool.urls", namespace="dubletten_tool")),
        ]

if "transkribus" in settings.INSTALLED_APPS:
    urlpatterns = urlpatterns + [
        url(r"^transkribus/", include("transkribus.urls")),
    ]

if "apis_bibsonomy" in settings.INSTALLED_APPS:
    urlpatterns.append(
        url(r"^bibsonomy/", include("apis_bibsonomy.urls", namespace="bibsonomy"))
    )

if "oebl_irs_workflow" in settings.INSTALLED_APPS:
    urlpatterns.append(
        url(
            r"^workflow/",
            include("oebl_irs_workflow.urls", namespace="oebl_irs_workflow"),
        )
    )

if "apis_ampel" in settings.INSTALLED_APPS:
    urlpatterns.append(
        url(
            r"^apis_ampel/",
            include("apis_ampel.urls", namespace="apis_ampel"),
        )
    )

# robots.txt route
# handling of robots.txt files on instance-basis can be configured in settings, see Readme.md
if os.path.exists(os.path.join(settings.ROBOTS_TXT_FOLDER,  "robots.txt")):
        urlpatterns.append(
    path("robots.txt", TemplateView.as_view(
    template_name="robots.txt", content_type="text/plain")),
    )

handler404 = "webpage.views.handler404"

