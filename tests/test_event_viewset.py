from datetime import date, timedelta

import pytest
from django.contrib.auth.backends import get_user_model
from django.shortcuts import reverse

from izba_docs_api.models import Document, Event, Tag

from .schemas import EVENT

TODAY = date.today()
UserModel = get_user_model()


@pytest.mark.django_db
def test_list(api_client, txt_file):
    user = UserModel.objects.create_user(username="foo", password="foo")
    api_client.force_authenticate(user)
    tag = Tag.objects.create(text="ham")

    for i in range(6):
        event = Event.objects.create(
            title=f"foobarbaz #{i + 1}",
            day=TODAY - timedelta(days=i),
            summary="spam & eggs",
        )
        event.visible_for.add(user) if i % 2 else None
        documents = [
            Document.objects.create(
                file=txt_file(),
                title=f"bazbarfoo #{j + 1}",
                description="eggs & spam",
                event=event,
            )
            for j in range(10)
        ]
        for j, document in enumerate(documents):
            document.tags.add(tag) if j % 2 else None

    response = api_client.get(reverse(f"izba_docs_api:event-list"))

    assert response.status_code == 200
    for e in response.data:
        EVENT.validate(e)
    assert len(response.data) == 3
