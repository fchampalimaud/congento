
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/', include('congentodb.urls')),

    path("accounts/", include("allauth.urls")),
    path("pyforms/", include("pyforms_web.web.urls")),
    path("", include("orquestra.urls")),
    path('admin/', admin.site.urls),
]
