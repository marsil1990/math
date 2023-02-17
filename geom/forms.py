from django import forms
from django.core.validators import validate_comma_separated_integer_list, RegexValidator


class Cuadrado(forms.Form):
    lado = forms.FloatField( label='')
    

class Triangulo_perimetro(forms.Form):
    lado1 = forms.FloatField(label='')
    lado2 = forms.FloatField(label='')
    lado3 =  forms.FloatField(label='')

class Triangulo_area(forms.Form):
    base  = forms.FloatField(label='base')
    altura = forms.FloatField(label='altura')
    
class Circulo(forms.Form):
    radio = forms.FloatField(label='')