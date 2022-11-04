from django import forms
from django.core import validators
from django.core.validators import RegexValidator

#Importar el modelo
from .models import Empleado

class EmpleadoForm(forms.Form):

    ESTADOS = [('activo', 'ACTIVO'),    ('despedido', 'DESPEDIDO'), ('vacaciones', 'VACACIONES')]

    nombre = forms.CharField(validators=[
        RegexValidator(regex='^[A-Z][a-z]*$', message='El nombre debe comenzar con mayúscula y no debe contener números'),
        validators.MinLengthValidator(3, 'El nombre debe tener al menos 3 caracteres'),
        validators.MaxLengthValidator(30, 'El nombre debe tener máximo 30 caracteres')
    ])
    apellido = forms.CharField(validators=[
        RegexValidator(regex='^[A-Z][a-z]*$', message='El nombre debe comenzar con mayúscula y no debe contener números'),
        validators.MinLengthValidator(3, 'El nombre debe tener al menos 3 caracteres'),
        validators.MaxLengthValidator(30, 'El nombre debe tener máximo 30 caracteres')
    ])
    departamento = forms.CharField(required=False)
    email = forms.EmailField(widget=forms.EmailInput)
    salario = forms.IntegerField(validators=[
        validators.MinValueValidator(200000, 'El salario debe ser mayor a 200K')    
        ])
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if nombre == 'Admin':
            raise forms.ValidationError('No se puede registrar a Admin')
        return nombre



    """ Aplicamos clases de bootstrap a los campos del formulario """
    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'
    departamento.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    salario.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

    ESTADOS = [('activo', 'ACTIVO'),    ('despedido', 'DESPEDIDO'), ('vacaciones', 'VACACIONES')]

    nombre = forms.CharField(validators=[
        RegexValidator(regex='^[A-Z][a-z]*$', message='El nombre debe comenzar con mayúscula y no debe contener números'),
        validators.MinLengthValidator(3, 'El nombre debe tener al menos 3 caracteres'),
        validators.MaxLengthValidator(30, 'El nombre debe tener máximo 30 caracteres')
    ])
    apellido = forms.CharField(validators=[
        RegexValidator(regex='^[A-Z][a-z]*$', message='El nombre debe comenzar con mayúscula y no debe contener números'),
        validators.MinLengthValidator(3, 'El nombre debe tener al menos 3 caracteres'),
        validators.MaxLengthValidator(30, 'El nombre debe tener máximo 30 caracteres')
    ])
    departamento = forms.CharField(required=False)
    email = forms.EmailField(widget=forms.EmailInput)
    salario = forms.IntegerField(validators=[
        validators.MinValueValidator(200000, 'El salario debe ser mayor a 200K')    
        ])
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if nombre == 'Admin':
            raise forms.ValidationError('No se puede registrar a Admin')
        return nombre


        
    """ Aplicamos clases de bootstrap a los campos del formulario """
    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'
    departamento.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    salario.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'