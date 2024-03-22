from django.db import models


class ExternalDB(models.Model):
    """Класс с параметрами запроса на подключение к БД пользователя"""
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    port = models.CharField(max_length=100) #Или Char?
    database_type = models.CharField(max_length=100)
    database_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class SQLQuery(models.Model):
    query = models.TextField()

    def __str__(self):
        return self.query
