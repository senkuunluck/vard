from rest_framework import serializers

from vard.models import File


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [('file')]