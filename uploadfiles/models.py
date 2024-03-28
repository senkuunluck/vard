from django.db import models
from django.core.validators import FileExtensionValidator


class UploadedFile(models.Model):
    file = models.FileField(upload_to="media/", validators=[FileExtensionValidator(allowed_extensions=['json', 'csv', 'xlsx'])])
    uploaded_on = models.DateTimeField(auto_now_add=True)

