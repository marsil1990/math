from django import forms
from django.core.validators import validate_comma_separated_integer_list, RegexValidator
class Datos(forms.Form):
    datos = forms.CharField(validators = [validate_comma_separated_integer_list], label= '')