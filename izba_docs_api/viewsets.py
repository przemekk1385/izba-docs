from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Document, Event, Tag
from .serializers import DocumentSerializer, EventSerializer, TagSerializer


# pylint: disable=too-many-ancestors
class DocumentViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = DocumentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Document.objects.filter(event__visible_for=self.request.user)


# pylint: disable=too-many-ancestors
class EventViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Event.objects.filter(visible_for=self.request.user)


# pylint: disable=too-many-ancestors
class TagViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = TagSerializer
    queryset = Tag.objects.all()
