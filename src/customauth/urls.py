"""
URL configuration for customauth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.conf import settings
from django.conf.urls.static import static

from apps.management.api.views import ObtainTokenView, HealthCheckView

urlpatterns = [
    path("admin/", admin.site.urls),
    # Healthcheck ENDPOINT(S)
    path("api/healthcheck/", HealthCheckView.as_view(), name="healthcheck"),
    # AUTH ENDPOINT(S)
    path("api/token/", ObtainTokenView.as_view(), name="obtain_token"),
    path("api/", include("apps.management.urls")),  # password change etc.
    path("api/management/", include("apps.management.api.urls")),
]
# API Doc (open api)
if settings.DEBUG == False:
    urlpatterns += (
        path(
            "api/docs/",
            get_schema_view(
                title=settings.APP_NAME,
                description="API Documentation",
                version="1.0.0",
                patterns=[
                    path("api/", include("apps.web.api.urls")),
                    path("api/token/", ObtainTokenView.as_view()),
                ],
            ),
            name="openapi-schema",
        ),
    )
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
