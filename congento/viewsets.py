from dynamic_rest.viewsets import DynamicModelViewSet

from fishdb.models import Species
from fishdb.models import Category

from .models import Fish
from .serializers.fish import FishSerializer


class BaseView(DynamicModelViewSet):
    ...


class FishViewSet(BaseView):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer
