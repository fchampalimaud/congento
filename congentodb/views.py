from .models import Fly, Rodent, Fish, Institution
from .serializers.fly import FlySerializer
from .serializers.rodent import RodentSerializer
from .serializers.fish import FishSerializer
from dynamic_rest.viewsets import DynamicModelViewSet
from dynamic_rest.viewsets import exceptions




class BaseView(DynamicModelViewSet):

    def perform_destroy(self, instance):

        if self.request.user.is_anonymous:
            raise exceptions.ValidationError("No institution associated to the user")

        try:
            institution = Institution.objects.get(user=self.request.user)
        except Institution.DoesNotExist:
            raise exceptions.ValidationError("No institution associated to the user")

        if instance.institution!=institution:
            raise exceptions.PermissionDenied('Objects deletion are allowed only for objects belonging the user institution.')

        return super().perform_destroy(instance)


    def get_queryset(self, queryset=None):

        queryset = super().get_queryset(queryset)

        if self.request.query_params.get('filter{remote_id}', False):

            try:
                institution = Institution.objects.get(user=self.request.user)
            except Institution.DoesNotExist:
                raise exceptions.PermissionDenied(
                    'Objects deletion are allowed only for objects belonging the user institution.')

            queryset = queryset.filter(institution=institution)

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

