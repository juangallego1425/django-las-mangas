from django import forms
from django.forms import fields
from captcha.fields import CaptchaField
from .models import Sugerencia


class SugerenciaForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Sugerencia
        fields = ["titulo", "descripcion"] 
        
        titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
