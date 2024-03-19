from rest_framework import serializers
from models import SQLQuery

class SQLQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = SQLQuery
        fields = '__all__'