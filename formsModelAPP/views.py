from django.shortcuts import redirect, render
from formsModelAPP.models import Empleado
from .forms import EmpleadoForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listadoEmpleados(request):
    listaEmpleados = Empleado.objects.all()
    data={'empleados':listaEmpleados}
    return render(request, 'empleados.html', data)

def crearEmpleado(request):
    form = EmpleadoForm()
    if (request.method == 'POST'):
        form = EmpleadoForm(request.POST)
        if (form.is_valid()):
            """ Rescatar los datos del formulario """
            emp = form.cleaned_data
            """ Crear el objeto empleado """
            empleado = Empleado(
                nombre = emp['nombre'],
                apellido = emp['apellido'],
                departamento = emp['departamento'],
                email = emp['email'],
                salario = emp['salario'],
                estado = emp['estado']
            )
            print("Datos validos")
            empleado.save()
            """Limpiar el formulario"""
            form = ''
            return redirect('/empleados')

    data = {'form':form, 'titulo':'Crear empleado'}
    return render(request, 'crearEmpleado.html', data)