from django.shortcuts import render, HttpResponseRedirect
from .forms import Cuadrado, Triangulo_area, Triangulo_perimetro, Circulo

# Create your views here.


def geom(request):
    cuadrado = Cuadrado()
    triangulo_a =  Triangulo_area()
    triangulo_p = Triangulo_perimetro()
    circulo =  Circulo()
    aux = 0
    if request.method == 'POST' and 'cuadrado_area' in request.POST:
        cuadrado = Cuadrado(request.POST)
        if cuadrado.is_valid():
           area_cuadrado  = cuadrado.cleaned_data['lado'] * cuadrado.cleaned_data['lado']
           aux = area_cuadrado
    elif request.method == 'POST' and 'cuadrado_perimetro' in request.POST:  
        cuadrado = Cuadrado(request.POST)
        if cuadrado.is_valid():
           perimetro_cuadrado  = cuadrado.cleaned_data['lado'] * 4
           aux = perimetro_cuadrado
          
    elif request.method == 'POST' and 'triangulo_perimetro' in request.POST:  
        triangulo_p = Triangulo_perimetro(request.POST)
        if triangulo_p.is_valid():
           perimetro_triangulo  = triangulo_p.cleaned_data['lado1'] + triangulo_p.cleaned_data['lado2'] + triangulo_p.cleaned_data['lado3'] 
           aux = perimetro_triangulo
         
    elif request.method == 'POST' and 'triangulo_area' in request.POST:  
        triangulo_a = Triangulo_area(request.POST)
        if triangulo_a.is_valid():
           area_triangulo  = (triangulo_a.cleaned_data['base'] * triangulo_a.cleaned_data['altura'])/2
           aux = area_triangulo
       
    elif request.method == 'POST' and 'circulo_area' in request.POST:  
        circulo = Circulo(request.POST)
        if circulo.is_valid():
           area_circulo  = circulo.cleaned_data['radio']*circulo.cleaned_data['radio']*3.14
           aux = area_circulo
       
    elif request.method == 'POST' and 'circulo_perimetro' in request.POST:  
        circulo = Circulo(request.POST)
        if circulo.is_valid():
           perimetro_circulo  = (circulo.cleaned_data['radio'] + circulo.cleaned_data['radio'])*3.14
           aux = perimetro_circulo
    
    cuadrado = Cuadrado()
    triangulo_a =  Triangulo_area()
    triangulo_p = Triangulo_perimetro()
    circulo =  Circulo()
           
    return render(request, 'geometria.html', {'cuadrado':cuadrado, 'triangulo_p':triangulo_p, 'triangulo_a':triangulo_a,  'circulo':circulo,  'aux':aux})