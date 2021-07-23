from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Document


def document_serve(_, path):
    document = get_object_or_404(Document, file=path)

    response = HttpResponse()
    response["Content-Disposition"] = f"attachment; filename={path}"
    response["X-Accel-Redirect"] = f"/{settings.MEDIA_ROOT}/{document.file}"

    return response
