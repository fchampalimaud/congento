
from dynamic_rest.serializers import DynamicRelationField

from .base import BaseSerializer

from ..models import Fish

class FishSerializer(BaseSerializer):
    # species = DynamicRelationField('FishSpeciesSerializer', deferred=False)

    class Meta:
        model = Fish
        name = 'fish'
        plural_name = 'fishes'
        fields = '__all__'
