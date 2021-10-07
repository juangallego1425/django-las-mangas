from django import forms
from django.forms import fields
from captcha.fields import CaptchaField
from django.forms.widgets import TextInput
from .models import Comentario


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class Comentario_via(forms.ModelForm):
    captcha = CaptchaField()
    
    class Meta:
        
        model= Comentario
        fields= ["titulo","fecha","descripcion" ]
        
        widgets = {
            'titulo':forms.TextInput(attrs={'class': 'input'}),
            'fecha': DateTimeInput(attrs={'class': 'form-control'})  
        }
  