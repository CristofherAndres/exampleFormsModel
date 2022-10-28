from django import forms

#Importar el modelo
from .models import Empleado

class EmpleadoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    email = forms.EmailField()
    salario = forms.IntegerField()
    estado = forms.CharField(max_length=50)