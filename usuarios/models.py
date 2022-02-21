from django.db import models

# Create your models here.
class Usuario(models.Model):
    tipo_genero = (
        ('M','Masculino'),
        ('F','Femenino'),
    )  
    foto = models.ImageField(upload_to='photos/%Y/%m/%d')
    nombre = models.CharField(max_length=100)
    profesion = models.CharField(max_length=150)
    genero = models.CharField(choices=tipo_genero, max_length=10)
    ciudad = models.CharField(max_length=100)