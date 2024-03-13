from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Files(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    place_id = models.AutoField()
    type_id = models.AutoField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)
    date_delete = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, unique=True)
    link = models.CharField(max_length=255, unique=True)
    publish = models.CharField(max_length=1, choices=TYPES)

class Access(models.Model):
    id_file = models.OneToOneField(Files, on_delete=models.CASCADE)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    access_type_id = models.AutoField()
    date_access_open = models.DateTimeField(auto_now=True)
    date_access_close = models.DateTimeField(auto_now=True)

class Feedback (models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    theme = models.CharField(max_length=255)
    description = models.TextField()

class Dushboards(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)

class Charts(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    file_id = models.OneToOneField(Files, on_delete=models.CASCADE)
    chart_id = models.OneToOneField(Charts, on_delete=models.CASCADE)
    dushboard_id = models.OneToOneField(Dushboards, on_delete=models.CASCADE)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    date_send = models.DateTimeField(auto_now=True)
    date_remove = models.DateTimeField(auto_now=True)
    date_delivery = models.DateTimeField(auto_now=True)
    comment = models.TextField()

class ReadComments(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    comment_id = models.OneToOneField(Comments, on_delete=models.CASCADE)
    date_reading = models.DateTimeField(auto_now=True)