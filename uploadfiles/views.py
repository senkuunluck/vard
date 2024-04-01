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