from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.
#Criar os bancos de dados 

#criar a lista de categorias 
LISTA_CATEGORIAS = (
    ("ANALISE", "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("ORGANIZACAO", "Organização"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),

)

class Filme(models.Model):
    titulo = models.CharField(max_length=400)
    thumb = models.ImageField(upload_to='thumb_field') #aqui foi o ultimo erro 
    descricao = models.TextField(max_length=10000)
    categoria = models.CharField(max_length=16, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.titulo}'


#criar os episodios 
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=400)
    video = models.URLField()

    def __str__(self):
        return f'{self.titulo} === {self.filme.titulo}'
     

class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")
