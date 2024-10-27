from django.shortcuts import render,redirect
from . import forms

from equipos.forms import FormularioEquipo
from equipos.models import Equipo

# Create your views here.

def index(request):
    return render (request,'equipos/index.html')

def listadoEquipos(request):
    equipos = Equipo.objects.all()
    data = {'equipos':equipos}
    return render (request,'equipos/equipos.html', data)

def agregarEquipos(request):
    form = FormularioEquipo()
    if request.method == 'POST':
        form = forms.FormularioEquipo(request.POST)
        if form.is_valid():
            form.save()
            return listadoEquipos(request)
    data= {'form':form}
    return render(request, 'equipos/agregarEquipo.html', data)

def eliminarEquipo(request,id):
    equipo = Equipo.objects.get(id=id)
    equipo.delete()
    return redirect('/equipos')

def actualizarEquipos(request,id):
    equipo = Equipo.objects.get(id=id)
    form = FormularioEquipo(instance=equipo)
    if request.method == 'POST':
        form = FormularioEquipo(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return listadoEquipos(request)
    
    data = {'form': form}
    return render(request, 'equipos/agregarEquipo.html', data)