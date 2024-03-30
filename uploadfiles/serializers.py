from rest_framework import serializers

from vard.models import File


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
        # не обрабатываем поле file_type.
        # Нельзя давать пользователю указывать произвольный тип файла, нужно вытаскивать его самим
        #см. views
#