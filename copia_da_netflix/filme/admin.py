from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin
# Register your models here.


#essa sessão só existe pq a gnt quer editar os usuários no painel de admin e tiver tbm o filmes vistos  
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ("filmes_vistos", )})
    ) #aqui define como vai aparecer no admin

UserAdmin.fieldsets = tuple(campos)

admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)





# como funciona o append no admin
# [
#     ("informações pessoais", {"fields": ("Primeiro nome", "Ultimo nome")})
# ]

