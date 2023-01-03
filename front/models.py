from django.db import models

from django.db import models
from django.forms import CharField, IntegerField


class Bancos(models.Model):
    nombreB = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreB


class Clientes(models.Model):
    nombreC = models.CharField(max_length=50)
    Cedula = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreC