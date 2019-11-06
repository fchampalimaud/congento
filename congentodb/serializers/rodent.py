from ..models import Rodent
from .base_serializer import BaseSerializer


class RodentSerializer(BaseSerializer):
    class Meta:
        model = Rodent
        name = "rodent"
        fields = (
            "id",
            "institution_name",
            "created",
            "modified",
            "availability",
            "link",
            "species",
            "strain_name",
            "common_name",
            "origin",
            "origin_other",
            "category",
            "background",
            "zygosity",
            "line_description",
            "coat_color",
            "reporter_gene",
            "inducible_cassette",
            "remote_id",
        )
