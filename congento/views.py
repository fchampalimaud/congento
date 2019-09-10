from django.shortcuts import render
from dynamic_rest.viewsets import DynamicModelViewSet

from .models import Fish
from .serializers.fish import FishSerializer


class BaseView(DynamicModelViewSet):
    ...

class FishViewSet(BaseView):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer

