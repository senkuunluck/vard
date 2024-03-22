from rest_framework import serializers
from IDE.models import SQLQuery, ExternalDB


class ExternalDBSerializer(serializers.ModelSerializer):
    model = ExternalDB
    fields = '__all__'


class SQLQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = SQLQuery
        fields = '__all__'