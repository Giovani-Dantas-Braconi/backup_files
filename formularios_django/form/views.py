from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormCadastro
# Create your views here.

def home(request):
    form = FormCadastro()
    return render(request, 'home.html', {"form":form})

def processa_form(request):
    form = FormCadastro(request.POST)
    if form.is_valid:
        nome = form.data["nome"]
        email = form.data["email"]
        return HttpResponse(f'{nome} {email}')
    return HttpResponse("Error")

def processa_form_db(request):
    form = FormCadastro(request.POST)
    if form.is_valid:
        form.save()
        return HttpResponse('salvo com sucesso')
    return HttpResponse("Error")