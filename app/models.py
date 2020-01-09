from django.db import models


# Create your models here.
class Person(models.Model):
    dni = models.CharField(primary_key=True, max_length=15)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
