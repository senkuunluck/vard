import requests
from rest_framework import serializers

from vard.models import File


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [('file')]

class LinkSerializer(serializers.Serializer):
    link = serializers.URLField()

    def validate_link(self, value):
        response = requests.head(value)
        if response.headers.get('Content-Type') is None:
            raise serializers.ValidationError("Invalid link provided. Content type not found.") # здесь доджим джанговские ограничения на Content Type
        return value