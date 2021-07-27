from rest_framework import routers

from . import viewsets

router = routers.DefaultRouter()
router.register("event", viewsets.EventViewSet, basename="event")
router.register("document", viewsets.DocumentViewSet, basename="document")
router.register("tag", viewsets.TagViewSet, basename="tag")
