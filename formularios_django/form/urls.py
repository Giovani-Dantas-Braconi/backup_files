from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('processa_form/', views.processa_form, name='processa_form'),
    path('processa_form_db/', views.processa_form_db, name="processa_form_db")
]
