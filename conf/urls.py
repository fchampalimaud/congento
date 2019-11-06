from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from users import views as users_views


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("sentry-debug/", trigger_error),
    path("api/", include("congentodb.urls")),
    path(
        "ajax/validate_institution/",
        users_views.validate_institution,
        name="validate_institution",
    ),
    path("accounts/", include("allauth.urls")),
    path("pyforms/", include("pyforms_web.web.urls")),
    path("", include("orquestra.urls")),
    path("admin/", admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
