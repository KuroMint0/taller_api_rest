from rest_framework import mixins, viewsets

from .models import Evento
from .serializers import EventoSerializer

class EventoViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Evento.objects.filter(activo=True)
    serializer_class = EventoSerializer