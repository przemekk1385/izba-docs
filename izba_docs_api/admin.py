from django.contrib import admin

from . import models


class InlineDocument(admin.StackedInline):

    extra = 1
    model = models.Document


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [InlineDocument]


admin.site.register(models.Document)
admin.site.register(models.Tag)
