from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.permissions import revoke_permission, grant_permission # o revoke serve para REVOGAR a permissão do admin, já o grant_permission ele adiciona uma permissão a um usuário 
from rolepermissions.decorators import has_role_decorator, has_permission_decorator #essas bibliotecas que permitem avaliar se o usuário tem o grupo ou se tem a permissoão RESPECTIVAMENTE 
# Create your views here.


#@has_permission_decorator('ver_metas')

def home(request):

    return render(request, 'home.html')

def criar_usuario(request):
    user = User.objects.create_user(username="caio", password="1234")
    user.save()
    assign_role(user,"gerente") # o assign_role serve para escolher o grupo que o usuário criado será inserido, 1° parametro deve ser qual usuário e o 2° param deve ser o grupo q ele representará NÃO SENDO A CLASS 
    return HttpResponse("user criado")
