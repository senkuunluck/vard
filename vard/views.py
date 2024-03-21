from django.shortcuts import render
from rest_framework import viewsets

from vard.serializers import *
from vard.models import *

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class FilesViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer

class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class DashboardsViewSet(viewsets.ModelViewSet):
    queryset = Dashboards.objects.all()
    serializer_class = DashboardsSerializer

class ChartsViewSet(viewsets.ModelViewSet):
    queryset = Charts.objects.all()
    serializer_class = ChartsSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

class ReadCommentsViewSet(viewsets.ModelViewSet):
    queryset = ReadComments.objects.all()
    serializer_class = ReadCommentsSerializer