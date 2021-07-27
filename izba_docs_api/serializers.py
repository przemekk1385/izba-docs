from rest_framework import serializers

from .models import Document, Event


class DocumentSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field="text")
    event = serializers.SlugRelatedField(read_only=True, slug_field="title")

    class Meta:

        fields = ("id", "file", "title", "description", "tags", "event")
        model = Document


class EventSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    documents = DocumentSerializer(many=True)

    class Meta:

        fields = ("id", "title", "day", "summary", "documents")
        model = Event
