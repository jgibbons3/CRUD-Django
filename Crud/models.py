from django.db import models

class Usuario(models.Model):
    name = models.CharField(max_length=20)
    apellido = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()

