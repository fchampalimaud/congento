from django.urls import include, path
from dynamic_rest import routers
from . import views

router = routers.DynamicRouter()
router.register(r'fly', views.FlyViewSet)
router.register(r'rodent', views.RodentViewSet)
router.register(r'fish', views.FishViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
