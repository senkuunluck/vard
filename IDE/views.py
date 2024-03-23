from rest_framework.views import APIView
from rest_framework.response import Response
import mysql.connector

from IDE.serializers import ExternalDBSerializer, SQLQuerySerializer

class ConnectToRemoteDB(APIView):
    """API для работы с IDE"""
    connection = None

    def establish_connection(self, host, user, password, database):
        """Функция для подключения к БД MySQL"""
        try:
            conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            return conn
        except mysql.connector.Error as e:
            return None

    def execute_sql_query(self, sql_query):
        """Функция для выполнения SQL-запросов"""
        cursor = self.connection.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def post(self, request):
        if request.path == 'api/v1/connect-to-external-db/': # этот кусок кода будет отрабатывать, когда пользователь подключается
            serializer = ExternalDBSerializer(data=request.data)
            if serializer.is_valid():
                data = serializer.validated_data

                self.connection = self.establish_connection(data['host'], data['user'], data['password'], data['database_name'])
                if self.connection is not None:
                    return Response("Connection successful")
                else:
                    return Response("Database connection error", status=500)

            return Response(serializer.errors, status=400)

        elif request.path == 'api/v1/execute-sql-query/': # этот кусок кода будет отрабатывать, когда пользователь передает запрос
            serializer = SQLQuerySerializer(data=request.data)
            if serializer.is_valid():
                data = serializer.validated_data

                result = self.execute_sql_query(data['query'])
                return Response(result)

            return Response(serializer.errors, status=400)