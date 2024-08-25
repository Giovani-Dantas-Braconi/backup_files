from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms 


class CriarContaform(UserCreationForm):
    email = forms.EmailField() # se nn for obrigatório colocar required=False
    
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2', ) #username, password1 e 2 são do propio django, é tipo o super 
        

class FormHome(forms.Form):
    email = forms.EmailField(label=False)