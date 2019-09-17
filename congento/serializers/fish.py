from .base import BaseSerializer

from ..models import Fish


class FishSerializer(BaseSerializer):
    class Meta:
        model = Fish
        name = "fish"
        plural_name = "fish"
        fields = "__all__"
