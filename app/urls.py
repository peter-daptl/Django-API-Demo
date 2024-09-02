"""Portfolio API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os

from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from app.utils.config import APIConfig

show_host = APIConfig.get_config_var("SHOW_HOSTNAME")

host_name = "Host: {host}".format(host=os.getenv("HOSTNAME")) if show_host else ""

schema_view = get_schema_view(
    openapi.Info(
        title="Portfolio Cycling API",
        default_version="",
        description=("Demo API Working in Tandem with Airflow Parser"),
    ),
    public=True,
)

urlpatterns = [
    path("", include("portfolio.urls")),
    re_path(
        r"^$",
        schema_view.with_ui("swagger", cache_timeout=None),
        name="schema-swagger-ui",
    ),
]
