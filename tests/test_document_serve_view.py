from datetime import date

import pytest
from django.contrib.auth.backends import get_user_model
from django.shortcuts import reverse

from izba_docs_api.models import Document, Event

TODAY = date.today()
UserModel = get_user_model()


@pytest.mark.django_db
def test_failed_401(api_client):
    response = api_client.get(
        reverse(f"izba_docs_api:document-serve", args=["foobarbaz"])
    )

    assert response.status_code == 401


@pytest.mark.django_db
def test_failed_403(api_client, txt_file):
    user = UserModel.objects.create_user(username="foo", password="foo")
    api_client.force_authenticate(user)

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

    assert response.status_code == 403


@pytest.mark.django_db
def test_failed_404(api_client):
    user = UserModel.objects.create_user(username="foo", password="foo")
    api_client.force_authenticate(user)

    response = api_client.get(
        reverse(f"izba_docs_api:document-serve", args=["foobarbaz"])
    )

    assert response.status_code == 404


@pytest.mark.django_db
def test_ok(api_client, txt_file):
    user = UserModel.objects.create_user(username="foo", password="foo")
    api_client.force_authenticate(user)

    event = Event.objects.create(
        title=f"foobarbaz",
        day=TODAY,
        summary="spam & eggs",
    )
    event.visible_for.add(user)
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
