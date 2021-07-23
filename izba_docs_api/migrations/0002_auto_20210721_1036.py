# Generated by Django 3.2.5 on 2021-07-21 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("izba_docs_api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="title",
            field=models.CharField(default="foo", max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="document",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]