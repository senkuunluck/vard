from rest_framework import serializers
from .models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'

class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class DashboardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboards
        fields = '__all__'

class ChartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charts
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class ReadCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadComments
        fields = '__all__'