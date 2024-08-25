from django.urls import path
from . import views

APP_NAME = 'app'
urlpatterns = [
    path('usuario/', views.criar_usuario, name="criar_usuario"),
    path('', views.home, name="home"),

]
