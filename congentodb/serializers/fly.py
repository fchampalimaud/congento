from ..models.fly import Fly
from .base_serializer import BaseSerializer

class FlySerializer(BaseSerializer):

    class Meta:
        model = Fly
        fields = (
            'id', 'institution_name',
            'created', 'modified', 'chrx',
            'chry', 'bal1', 'chr2', 'bal2',
            'chr3', 'bal3', 'chr4', 'chru',
            'legacy1', 'legacy2', 'legacy3',
            'flydbid',
            'genotype', 'category', 'specie',
            'remote_id'
        )