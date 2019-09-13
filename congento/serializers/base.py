from dynamic_rest.serializers import DynamicModelSerializer

# from rest_framework import serializers
# from ..models import Institution


class BaseSerializer(DynamicModelSerializer):
    pass

    # id = serializers.ReadOnlyField()
    # institution_name = serializers.ReadOnlyField()

    # def validate(self, data):
    #     request = self.context.get('request')

    #     if request.user.is_anonymous:
    #         raise serializers.ValidationError("No institution associated to the user")

    #     try:
    #         Institution.objects.get(user=request.user)
    #     except Institution.DoesNotExist:
    #         raise serializers.ValidationError("No institution associated to the user")

    #     return data

    # def update(self, instance, data):
    #     request = self.context.get('request')

    #     if instance.institution != Institution.objects.get(user=request.user):
    #         raise serializers.ValidationError("No permission to update this register")

    #     return super().update(instance, data)

    # def create(self, data):
    #     request = self.context.get('request')
    #     data['institution'] = Institution.objects.get(user=request.user)
    #     return super().create(data)
