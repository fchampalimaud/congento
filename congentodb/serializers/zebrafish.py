from .base_serializer import BaseSerializer
from ..models.zebrafish import Zebrafish

class ZebrafishSerializer(BaseSerializer):

    class Meta:
        model = Zebrafish
        fields = (
            'id', 'institution_name',
            'created', 'modified', 'background',
            'genotype', 'phenotype', 'origin', 'availability',
            'comments', 'link', 'mta', 'line_name',
            'line_number', 'line_type', 'line_type_other',
            'remote_id'
        )