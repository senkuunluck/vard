from rest_framework.views import APIView
from rest_framework.response import Response
import pymysql
from IDE.serializers import ExternalDBSerializer, SQLQuerySerializer

class DatabaseConnectionView(APIView):
    """АПИ для подключения к пользовательской БД"""
    def post(self, request):
        serializer = ExternalDBSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            connection_data = {
                'database': data['database_name'],
                'user': data['user'],
                'password': data['password'],
                'host': data['host'],
                'port': data['port']
            } # Берем всю информацию, которая нужна для полключения к серверу БД MYSQL
            try:
                connection = pymysql.connect(**connection_data) #Подключаемся
                request.external_db_connection = connection  # Сохраняем подключение в аттрибуте объекта реквест (Костыль пиздец, хз сработает ли)
                return Response({'message': 'Successfully connected to the MySQL database'})
            except pymysql.Error as e:
                return Response({'message': f'Error connecting to the MySQL database: {str(e)}'}, status=400)
        else:
            return Response(serializer.errors, status=400)

class SQLQueryView(APIView):
    """АПИ для отправки запросов к пользовательской БД"""
    def post(self, request):
        serializer = SQLQuerySerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.validated_data.get('query')
            try:
                with request.external_db_connection.cursor() as cursor:  #Подключаемся
                    cursor.execute(query)
                    results = cursor.fetchall()
                    return Response({'results': results})
            except pymysql.Error as e:
                return Response({'message': f'Error executing SQL query: {str(e)}'}, status=400)
        else:
            return Response(serializer.errors, status=400)