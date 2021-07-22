from rest_framework import viewsets

from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = EventSerializer
    queryset = Event.objects.all()
