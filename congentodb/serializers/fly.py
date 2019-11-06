from ..models.fly import Fly
from .base_serializer import BaseSerializer


class FlySerializer(BaseSerializer):
    class Meta:
        model = Fly
        fields = (
            "id",
            "institution_name",
            "created",
            "modified",
            "chrx",
            "chry",
            "bal1",
            "chr2",
            "bal2",
            "chr3",
            "bal3",
            "chr4",
            "chru",
            "categories",
            "species",
            "origin",
            "genotype",
            "origin_center",
            "remote_id",
            "special_husbandry_conditions",
            "line_description",
        )
