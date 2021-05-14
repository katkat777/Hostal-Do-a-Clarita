from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(max_length=11, unique=True)
    nombre = models.CharField(max_length=50)
    apellido =models.CharField(max_length=50)

