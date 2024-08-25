from django.db import models
from django.contrib.auth.models import User 


# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    telefone = models.EmailField(max_length=200, blank=True, null=True)
    id_sessao = models.CharField(max_length=200, blank=True, null=True)
    usuario = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}'

class Categoria(models.Model): # (masculino, feminio, infatil)
    nome = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.nome}'

class Tipo(models.Model): # (calça, camisa, bermuda)
    nome = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.nome}'

class Produto(models.Model):
    imagem = models.ImageField(blank=True, null=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.SET_NULL)
    tipo = models.ForeignKey(Tipo, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'Nome: {self.nome}, Categoria: {self.categoria}, Tipo: {self.tipo}, Preço: {self.preco}'

class ItemEstoque(models.Model):
    produto = models.ForeignKey(Produto, blank=True, null=True, on_delete=models.SET_NULL)
    cor = models.CharField(max_length=200, blank=True, null=True)
    tamanho = models.CharField(max_length=200, blank=True, null=True)
    quantidade = models.IntegerField(default=0)

class Endereco(models.Model):
    rua = models.CharField(max_length=400, null=True, blank=True)
    numero = models.IntegerField(default=0)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    cep = models.IntegerField(null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=200, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.SET_NULL)


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    finalizado = models.BooleanField(default=False)
    id_transacao = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, blank=True, null=True, on_delete=models.SET_NULL)
    data_finalizacao = models.DateTimeField(blank=True, null=True)

class ItensPedido(models.Model):
    item_estoque = models.ForeignKey(ItemEstoque, blank=True, null=True, on_delete=models.SET_NULL)
    quantidade = models.IntegerField(default=0)
    pedido = models.ForeignKey(Pedido, blank=True, null=True, on_delete=models.SET_NULL)



#Cliente 
    # nome
    # email
    # telefone 
    # usuario

#Produto 
    # imagem 
    # nome 
    # preco 
    # ativo 

#Categoria (masculino, feminio, infatil)
    #nome

#Tipo (calça, camisa, bermuda)
    #nome 

#ItemEstoque
    # produto (camisa)
    # cor (azul, laranja, verde)
    # tamanho (P, M, G)
    # quantidade


#ItensPedido
    # itemestoque 
    # quantidade

#Pedido 
    # cliente 
    # data_finalizacao 
    # finalizado 
    # id_transacao
    # endereco 
    # itenspedido 


#Endereco 
    # rua 
    # numero 
    # complemento 
    # cep 
    # cidade 
    # estado 
    # cliente 