from django import forms
from .models import Pessoa

class FormCadastro (forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField()


class FormCadastroDB(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ("nome", "email")