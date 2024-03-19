from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SQLQuerySerializer
from django.db import connection

class SQLQueryView(APIView):
    def post(self, request):
        serializer = SQLQuerySerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.validated_data.get('query')
            try:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    results = cursor.fetchall()
                    return Response({"results": results})
            except Exception as e:
                return Response({"error": str(e)}, status=400)
        return Response(serializer.errors, status=400)