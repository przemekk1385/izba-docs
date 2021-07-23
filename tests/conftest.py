from random import choice
from typing import Callable
from uuid import uuid4

import pytest
from django.core.files import File
from rest_framework.test import APIClient


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def txt_file(tmp_path) -> Callable:
    def make_attachment_file(chars: int = 4096) -> File:
        path = tmp_path / f"{uuid4()}.txt"

        with open(path, "w") as f:
            f.write(
                "".join(
                    [
                        choice("abcdefghijklmnopqrstuvwxyz1234567890")
                        for _ in range(chars)
                    ]
                )
            )
            f.close()

        return File(open(path, "r"))

    yield make_attachment_file
