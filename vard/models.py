from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import FileExtensionValidator


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_passwords_change = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            MyUser.objects.create(user=instance)
            instance.save()



class File(models.Model):
    CSV = 'CSV'
    JSON = 'JSON'
    EXCEL = 'EXCEL'
    PDF = 'PDF'
    COMMUNITY = 'COM'
    MY_FILES = 'MFL'
    BEST_PRACTICES = 'BPS'

    PLACE = [
        (COMMUNITY, 'Community'),
        (MY_FILES, 'My_files'),
        (BEST_PRACTICES, 'Best_Practices')
    ]

    FILE_TYPE = [
        (CSV, 'CSV'),
        (JSON, 'JSON'),
        (EXCEL, 'EXCEL'),
        (PDF, 'PDF'),
    ]
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    place = models.CharField(max_length=3, choices=PLACE, default='MFL')
    file_type = models.CharField(max_length=10, choices=FILE_TYPE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)
    date_delete = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to= 'media/',
                            unique=True,
                            validators=[FileExtensionValidator
                                        (allowed_extensions=['json', 'csv', 'xlsx', 'pdf'])])
    link = models.CharField(max_length=255, default='Local File')
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.link

class Access(models.Model):
    READER = 'RDR'
    OWNER = 'OWN'
    COMMENTATOR = 'CMT'
    EDITOR = 'EDT'

    ACCESS_TYPES = [
        (READER, 'READER'),
        (OWNER, 'OWNER'),
        (COMMENTATOR, 'COMMENTATOR'),
        (EDITOR, 'EDITOR'),
    ]
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    access_type = models.CharField(max_length=20, choices=ACCESS_TYPES)
    date_access_open = models.DateTimeField(auto_now=True)
    date_access_close = models.DateTimeField(auto_now=True)


class Feedback(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    theme = models.CharField(max_length=255)
    description = models.TextField()


class Dashboard(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)


class Chart(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_send = models.DateTimeField(auto_now=True)
    date_remove = models.DateTimeField(auto_now=True)
    date_delivery = models.DateTimeField(auto_now=True)
    comment = models.TextField()


class ReadComment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    date_reading = models.DateTimeField(auto_now=True)

