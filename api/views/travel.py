from rest_framework import viewsets, permissions
from ..serializers import TravelSerializer, RuteSerializer,RutaCreateSerializer,ServiceCreateSerializer,serviceSerializer
from ..permisions import IsOwner
from ..models import Travel,Rute,Service

# Create your views here.

class TravelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows devices to be viewed or edited.
    """
    serializer_class = TravelSerializer
    permission_classes = (
        IsOwner,
        permissions.IsAuthenticated,
    )


    def get_queryset(self):
        """
        Filter devices of the user that made the request.
        """
        return Travel.objects.all().filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_context(self):
        context = super(TravelViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context        


class RuteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows device data to be viewed or edited.
    """
    serializer_class = RutaCreateSerializer
    permission_classes = (
            permissions.IsAuthenticated,
        )

    serializer_action_classes={
        "list": RuteSerializer,
    }
    def get_queryset(self):
        """
        Filter data of devices that belongs to user who made the request.
        """
        return Rute.objects.all().filter(viaje__user=self.request.user)
    
    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()


class ServicioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows device data to be viewed or edited.
    """
    serializer_class = ServiceCreateSerializer
    permission_classes = (
            permissions.IsAuthenticated,
        )

    serializer_action_classes={
        "list": serviceSerializer,
    }
    def get_queryset(self):
        """
        Filter data of devices that belongs to user who made the request.
        """
        return Service.objects.all().filter(viaje__user=self.request.user)
    
    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()