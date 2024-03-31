from requests import get
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from vard.models import File
from .serializers import FileUploadSerializer


class FileUploadView(APIView):
    '''API для загрузки файлов на сервер напрямую от пользователя'''
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        file_serializer = self.serializer_class(data=request.data)

        if file_serializer.is_valid():

            user = request.user
            my_user = user.myuser

            file_obj = request.FILES['link']
            file_content = file_obj.read()
            file_name = default_storage.save(file_obj.name, ContentFile(file_content))

            if file_name.endswith('.xlsx'):
                file_type = 'EXCEL'
            elif file_name.endswith('.pdf'):
                file_type = 'PDF'
            elif file_name.endswith('.csv'):
                file_type = 'CSV'
            elif file_name.endswith('.json'):
                file_type = 'JSON'

            file_url = default_storage.url(file_name)

            file_serializer.save(link=file_url, name = file_name, user = my_user, file_type = file_type)

            return Response(file_serializer.data, status=status.HTTP_201_CREATED)

        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DownloadFromApi(APIView):

    def post(self, request, *args, **kwargs):
        # Получаем данные из тела запроса
        link = request.data.get('link')
        place = request.data.get('place')
        file_type = request.data.get('file_type')
        file_name = request.data.get('file_name')

        if not link:
            return Response({"error": "Link is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Скачивание файла по ссылке
        response = get(link)
        if response.status_code == 200:
            # Создание экземпляра модели File и заполнение его полями
            file_instance = File()
            file_instance.user = request.user  # Авторизованный пользователь
            file_instance.place = place
            file_instance.file_type = file_type
            file_instance.name = file_name
            # Сохранение файла, полученного по ссылке
            file_content = ContentFile(response.content)
            file_instance.link.save(file_name, file_content)

            file_instance.save()
            return Response({"success": "File saved successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Failed to download the file"}, status=response.status_code)