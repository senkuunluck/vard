import os

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from vard.models import File
from .serializers import FileUploadSerializer, LinkSerializer


class FileUploadView(APIView):
    '''API для загрузки файлов на сервер напрямую от пользователя'''
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        file_serializer = self.serializer_class(data=request.data)

        if file_serializer.is_valid():

            user = request.user
            my_user = user.myuser

            file_obj = request.FILES['file']
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


class UploadViaLink(APIView):
    def post(self, request):
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            link = serializer.validated_data['link']
            file_name = link.split('/')[-1]
            try:
                response = requests.get(link)

                file = File(name=file_name, user=request.user.myuser)
                file.file.save(file_name, ContentFile(response.content))
                file.save()
                _, file_extension = os.path.splitext(file_name)
                file_extension = file_extension.lower()

                file_type = None
                if file_extension == '.xlsx':
                    file_type = 'EXCEL'
                elif file_extension == '.pdf':
                    file_type = 'PDF'
                elif file_extension == '.csv':
                    file_type = 'CSV'
                elif file_extension == '.json':
                    file_type = 'JSON'

                # Сохранение типа файла
                if file_type:
                    file.file_type = file_type
                    file.save()

                return Response('File added')
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)