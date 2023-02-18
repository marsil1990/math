# Create your views here.
from django.shortcuts import render
from .forms import Datos
import numpy as np
from .moda import mode
#[2,2,2,3,3,3,3]
    
def est(request):
    data = Datos()
    obtener_datos_formulario = ''
    lista_numeros = []
    if request.method == 'POST':
        data = Datos(request.POST)
        if data.is_valid():
           obtener_datos_formulario = data.cleaned_data['datos'] #una cadena de caracteres
           obtener_datos_formulario = obtener_datos_formulario.split(',')
           for n in obtener_datos_formulario:  # transformamos la cade de caracteres en una lista de numeros
               lista_numeros.append(float(n))
    data = Datos()
    array_datos = np.array(lista_numeros)
    moda = []
    moda = mode(lista_numeros)
    mediana = np.median(array_datos)
    media = array_datos.mean()
    varianza = array_datos.var()
    desviacion = array_datos.std()
    cv = desviacion/media
    
    

    
    
    return render(request, 'estadistica.html', context = {'data':data,'mediana':mediana, 'media':media, 'varianza':varianza, 'desviacion':desviacion,
                                                'cv':cv, 'moda':moda})
