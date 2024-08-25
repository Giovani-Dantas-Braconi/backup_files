from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

def enviar_email(request):
    send_mail('Assunto', 'Eu lhe mandei um e-mail', "Giovanidbraconi@gmail.com", ["gabrielatrusgarcia@gmail.com"]) #1° assunto, 2° Corpo do texto, 3° quem ta mandando e 4° é OBRIGATORIAMENTE uma LISTA mas pode contar apenas 1 
    return HttpResponse("Olá")