from dynamic_rest.viewsets import DynamicModelViewSet

from fishdb.models import Species
from fishdb.models import Category

from .models import Fish
from .serializers.fish import FishSerializer
from .serializers.fish import FishSpeciesSerializer
from .serializers.fish import FishCategorySerializer


class BaseView(DynamicModelViewSet):
    ...


class FishViewSet(BaseView):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer


class FishSpeciesViewSet(BaseView):
    queryset = Species.objects.all()
    serializer_class = FishSpeciesSerializer


class FishCategoryViewSet(BaseView):
    queryset = Category.objects.all()
    serializer_class = FishCategorySerializer
