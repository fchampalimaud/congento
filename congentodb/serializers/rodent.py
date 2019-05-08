from ..models import Rodent
from .base_serializer import BaseSerializer

class RodentSerializer(BaseSerializer):

    class Meta:
        model = Rodent
        name = 'rodent'
        fields = ( 'id', 'institution_name',
            'created', 'modified', 'species',
            'strain_name', 'common_name', 'origin', 'availability',
            'comments', 'link', 'mta', 'background',
            'background_other', 'genotype', 'genotype_other',
            'model_type', 'model_type_other', 'remote_id'
        )