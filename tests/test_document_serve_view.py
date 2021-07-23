from datetime import date

import pytest
from django.shortcuts import reverse

from izba_docs_api.models import Document, Event

TODAY = date.today()


@pytest.mark.django_db
def test_failed(api_client):
    response = api_client.get(
        reverse(f"izba_docs_api:document-serve", args=["foobarbaz"])
    )

    assert response.status_code == 404


@pytest.mark.django_db
def test_ok(api_client, txt_file):
    event = Event.objects.create(
        title=f"foobarbaz",
        day=TODAY,
        summary="spam & eggs",
    )
    document = Document.objects.create(
        file=txt_file(),
        title=f"bazbarfoo",
        description="eggs & spam",
        event=event,
    )

    response = api_client.get(
        reverse(f"izba_docs_api:document-serve", args=[document.file])
    )

    assert response.status_code == 200
    assert (
        f"attachment; filename={document.file}"
        in response.headers["Content-Disposition"]
    )
