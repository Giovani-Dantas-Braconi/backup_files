from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.enviar_email, name="home")
]
