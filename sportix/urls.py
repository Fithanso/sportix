from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Sportix API",
        default_version='v1',
        description="First version of Sportix Application Programming Interface",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@sportix.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    url='http://127.0.0.1:8000/'
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path("api/v1/accounts/", include('apps.accounts.urls')),
    path("api/v1/sports/", include('apps.sports.urls')),
]
