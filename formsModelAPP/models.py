from django.db import models

# Create your models here.
# Modelo de empleados

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    email = models.EmailField()
    salario = models.IntegerField()
    estado = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre
        
