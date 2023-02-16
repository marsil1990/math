from django.shortcuts import render, HttpResponse
# Create your views here.
from .models import Project

def perfil(request):
    proyectos = Project.objects.all()
    return render(request, 'profile.html', {'proyectos':proyectos})