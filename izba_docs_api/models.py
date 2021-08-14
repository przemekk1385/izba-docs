from pathlib import Path
from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.deconstruct import deconstructible

User = get_user_model()
DATE_FORMAT = "%Y-%m-%d"


# pylint: disable=too-few-public-methods
@deconstructible
class Uuid4Path:
    def __call__(self, instance, filename):
        return Path("{}.{}".format(uuid4(), filename.split(".")[-1])).as_posix()


class Event(models.Model):

    title = models.CharField(max_length=100)
    day = models.DateField()
    summary = models.TextField()

    # related
    visible_for = models.ManyToManyField(User)

    class Meta:

        ordering = ("-day", "-id")

    def __str__(self):
        return "{} {}".format(self.day.strftime(DATE_FORMAT), self.title)

    def __repr__(self):
        return ("<Event id={} title={} day={}>").format(
            self.id,
            self.title,
            self.day.strftime(DATE_FORMAT),
        )


class Tag(models.Model):

    text = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.text)

    def __repr__(self):
        return "<Tag id={} text={}>".format(self.id, self.text)


class Document(models.Model):

    file = models.FileField(max_length=200, upload_to=Uuid4Path())
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    # related
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="documents")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return "{} {}".format(self.file, self.title)

    def __repr__(self):
        return "<Document id={} file={} title={}>".format(
            self.id, self.file, self.title
        )
