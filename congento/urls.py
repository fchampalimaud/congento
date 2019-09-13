from django.urls import include, path

from dynamic_rest import routers

from . import viewsets

router = routers.DynamicRouter()

router.register('fish', viewsets.FishViewSet)
router.register('fish-species', viewsets.FishSpeciesViewSet)
router.register('fish-categories', viewsets.FishCategoryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
