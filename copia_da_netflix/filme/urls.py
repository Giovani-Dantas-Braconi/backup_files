# criar uma URL 
#criar uma view (oq acontece se a pessoa entrar no link(python))
#criar um template (html, css, js)

from django.urls import path, include, reverse_lazy
from .views import Homepage, Homefilmes, Detalhesfilmes, Pesquisafilme, Editarperfil, Criarconta
from django.contrib.auth import views as Auth_view

app_name = "filme"

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilmes.as_view(), name='detalhesfilmes'),
    path('pesquisa/', Pesquisafilme.as_view(), name='pesquisafilme'),
    path('login/', Auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', Auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
    path('editarperfil/<int:pk>', Editarperfil.as_view(), name='editarperfil'),
    path('mudar_senha', Auth_view.PasswordChangeView.as_view(template_name='editarperfil.html', success_url=reverse_lazy(' filme:homefilmes')), name='mudarsenha'), #se for uma view padrão do django com o caso do PasswordChangeView pode passar o success_url =reverse_lazy(' filme:homefilmes') para definir qual pagina ele vai dps de concluir o forms 

]