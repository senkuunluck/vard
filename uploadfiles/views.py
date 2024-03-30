import magic
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from .serializers import FileUploadSerializer


class FileUploadView(APIView):
    '''API для загрузки файлов на сервер напрямую от пользователя'''
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        file_serializer = self.serializer_class(data=request.data)

        if file_serializer.is_valid():
            file_obj = request.FILES['link']  # Создаем объект файла в Django.
            file_content = file_obj.read()
            file_name = default_storage.save(file_obj.name, ContentFile(file_content))
            # здесь мы сохраняем файл в виде объекта джанго. Певый аргумент - это путь, второй - сам файл.
            # сам файл оборачивается в ContentFile - джанговский класс для работы с файлами
            # .read() - его содержимое

            file_url = default_storage.url(file_name)
            # говорим джанго сгенерировать урл для доступа к файлу

            file_serializer.save(link=file_url)
            # сохраняем всё что вытащили

            return Response(file_serializer.data, status=status.HTTP_201_CREATED)

        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
