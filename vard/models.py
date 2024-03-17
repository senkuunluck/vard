from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_passwords_change = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=255)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Users.objects.create(user=instance)
            instance.users.save()



class Place(models.Model):
    type = models.CharField(max_length=255)

class Access_type(models.Model):
    access_type = models.CharField(max_length=255)

class Files_type(models.Model):
    files_type = models.CharField(max_length=255)

class Files(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    type = models.ForeignKey(Access_type, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)
    date_delete = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, unique=True)
    link = models.CharField(max_length=255, unique=True)
    publish = models.BooleanField(default=True) #TODO

class Access(models.Model):
    id_file = models.ForeignKey(Files, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    access_type_id = models.ForeignKey(Access_type, on_delete=models.CASCADE)
    date_access_open = models.DateTimeField(auto_now=True)
    date_access_close = models.DateTimeField(auto_now=True)

class Feedback (models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    theme = models.CharField(max_length=255)
    description = models.TextField()

class Dushboards(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)

class Charts(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    file = models.ForeignKey(Files, on_delete=models.CASCADE)
    chart = models.ForeignKey(Charts, on_delete=models.CASCADE)
    dushboard = models.ForeignKey(Dushboards, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date_send = models.DateTimeField(auto_now=True)
    date_remove = models.DateTimeField(auto_now=True)
    date_delivery = models.DateTimeField(auto_now=True)
    comment = models.TextField()

class ReadComments(models.Model): #TODO
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    date_reading = models.DateTimeField(auto_now=True)

