from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_creacion_registro= models.DateField(null=True)
    parentesco = models.CharField(max_length=10)
    
