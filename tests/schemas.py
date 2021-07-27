from datetime import datetime

from django.conf import settings
from schema import And, Schema, Use


def positive(num: int) -> bool:
    return num > 0


DOCUMENT = Schema(
    {
        "id": And(Use(int), positive),
        "file": And(str, len),
        "title": And(str, len),
        "description": And(str, len),
        "tags": [str],
        "event": And(str, len),
    }
)

EVENT = Schema(
    {
        "id": And(Use(int), positive),
        "title": And(str, len),
        "day": And(
            Use(
                lambda day: datetime.strptime(
                    day, settings.REST_FRAMEWORK["DATE_FORMAT"]
                ).date()
            )
        ),
        "summary": And(str, len),
        "documents": [DOCUMENT],
    }
)
