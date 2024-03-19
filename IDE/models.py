from django.db import models

class SQLQuery(models.Model):
    query = models.TextField()

    def __str__(self):
        return self.query
