from .base_serializer import BaseSerializer
from ..models.fish import Fish

class FishSerializer(BaseSerializer):

    class Meta:
        model = Fish
        fields = (
            'id', 'institution_name',

            "created",
            "modified",
            "availability",
            "link",
            "strain_name",
            "common_name",
            "background",
            "genotype",
            "phenotype",
            "origin",
            "quarantine",
            "mta",
            "line_description",
            "category_name",
            "species_name",

            'remote_id'
        )
