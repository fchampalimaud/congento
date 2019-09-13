from dynamic_rest.serializers import DynamicRelationField

from .base import BaseSerializer

from ..models import Fish
from ..models import Category
from ..models import Species


class FishCategorySerializer(BaseSerializer):
    class Meta:
        model = Category
        name = "category"
        plural_name = "categories"
        fields = "__all__"

    fish = DynamicRelationField(
        "FishSerializer", source="congento_fish_related", many=True, deferred=True
    )


class FishSpeciesSerializer(BaseSerializer):
    class Meta:
        model = Species
        name = "species"
        plural_name = "species"
        fields = "__all__"

    fish = DynamicRelationField(
        "FishSerializer", source="congento_fish_related", many=True, deferred=True
    )


class FishSerializer(BaseSerializer):
    class Meta:
        model = Fish
        name = "fish"
        plural_name = "fish"
        fields = "__all__"

    category_id = DynamicRelationField("FishCategorySerializer")
    species_id = DynamicRelationField("FishSpeciesSerializer")
