from dynamic_rest.viewsets import DynamicModelViewSet
from dynamic_rest.viewsets import exceptions

from .models import CongentoMember, Fly, Rodent, Fish
from .serializers.fly import FlySerializer
from .serializers.rodent import RodentSerializer
from .serializers.fish import FishSerializer


class BaseView(DynamicModelViewSet):
    def perform_destroy(self, instance):

        if self.request.user.is_anonymous:
            raise exceptions.ValidationError("No institution associated to the user")

        try:
            congento_member = CongentoMember.objects.get(api_user=self.request.user)
        except CongentoMember.DoesNotExist:
            raise exceptions.ValidationError("No institution associated to the user")

        if instance.congento_member != congento_member:
            raise exceptions.PermissionDenied(
                "Objects deletion are allowed only for objects belonging the user institution."
            )

        return super().perform_destroy(instance)

    def get_queryset(self, queryset=None):

        queryset = super().get_queryset(queryset)

        if self.request.query_params.get("filter{remote_id}", False):

            try:
                congento_member = CongentoMember.objects.get(api_user=self.request.user)
            except CongentoMember.DoesNotExist:
                raise exceptions.PermissionDenied(
                    "Objects deletion are allowed only for objects belonging the user institution."
                )

            queryset = queryset.filter(congento_member=congento_member)

        return queryset


class FlyViewSet(BaseView):
    queryset = Fly.objects.all()
    serializer_class = FlySerializer


class RodentViewSet(BaseView):
    queryset = Rodent.objects.all()
    serializer_class = RodentSerializer


class FishViewSet(BaseView):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer
