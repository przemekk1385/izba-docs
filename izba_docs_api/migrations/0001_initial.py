# Generated by Django 3.2.5 on 2021-07-20 19:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import izba_docs_api.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("day", models.DateField()),
                ("summary", models.TextField()),
                ("visible_for", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "ordering": ("-day", "-id"),
            },
        ),
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        max_length=200, upload_to=izba_docs_api.models.Uuid4Path()
                    ),
                ),
                ("description", models.CharField(max_length=200)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="documents",
                        to="izba_docs_api.event",
                    ),
                ),
                ("tags", models.ManyToManyField(to="izba_docs_api.Tag")),
            ],
        ),
    ]
