from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from .models import Document


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def document_serve(request, path):
    document = get_object_or_404(Document, file=path)

    if request.user not in document.event.visible_for.all():
        raise PermissionDenied(_("Forbidden."))

    response = HttpResponse()
    response["Content-Disposition"] = f"attachment; filename={path}"
    response["X-Accel-Redirect"] = f"/{settings.MEDIA_ROOT}/{document.file}"
    return response
