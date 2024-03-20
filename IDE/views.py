#from MySQLdb import connections
from rest_framework.views import APIView
from rest_framework.response import Response
from IDE.serializers import SQLQuerySerializer
from django.db import connections

class SQLQueryView(APIView):
    def post(self, request):
        serializer = SQLQuerySerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.validated_data.get('query')
            try:
                with connections['external_db'].cursor() as cursor:
                    cursor.execute(query)
                    results = cursor.fetchall()
                    return Response({"results": results})
            except Exception as e:
                return Response({"error": str(e)}, status=500) #TODO
        return Response(serializer.errors, status=400)