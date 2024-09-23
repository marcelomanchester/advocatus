from django.db import models

class Clients(models.Model):

    name = models.CharField(max_length=255, unique=True)
    number = models.CharField(max_length=255, unique=True)
    birthdate = models.DateTimeField()
    role = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255, unique=True)
    adress = models.CharField(max_length=255)
    complement = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    document_id = models.CharField(max_length=255, unique=True)