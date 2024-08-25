from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Filme, Usuario
from django.views.generic import TemplateView, CreateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriarContaform, FormHome


# Create your views here.





class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHome


    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated: #se o ususário estiver autenticado 
            return redirect('filme:homefilmes') #redireciona para a homefilmes 
        else:
            return super().get(request, *args, **kwargs) #redireicona pra homepage 
    

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')



class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme

    #object_list => Lista de Objectos (lista de itens do modelo) - Mais geralzão do models


class Detalhesfilmes(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilmes.html"
    model = Filme

    def get(self, request, *args, **kwargs):    
        filme = self.get_object() #descobrir qual filme ta olhando 
        filme.visualizacoes += 1 # somar 1 as views daqle filme
        filme.save() #salvar  

        usuario = request.user
        usuario.filmes_vistos.add(filme)


        return super().get(request, *args, **kwargs) #redireiciona para o link final 

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilmes, self).get_context_data(**kwargs)
        # juntar todos os filmes que são da mesma categoria, usando o OBJECT, signfica WHERE categoria == Categoria
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[:5]#caso quiser pode usar os ngc de limite [0:3] por exemplo 

        context["filmes_relacionados"] = filmes_relacionados 
        return context 

    #object => 1 objeto (1 item do nosso modelo)


class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme 

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = Filme.objects.filter(titulo__icontains=termo_pesquisa) #está verificando se o texto digitado CONTEM no campo TITULO o texto 
            return object_list
        else:
            return None
        




class Editarperfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']


    def get_success_url(self):
        return reverse('filme:homefilmes')




class Criarconta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaform 
    # É uma boa prática pra formulários que quem decide os campos somos nós, é comum criar os forms em arquivos PYTHON de fora 
    
    def form_valid(self, form):
        form.save() #tem q salvar para adicionar o usuário no banco de dados 
        return super().form_valid(form)
    

    def get_success_url(self):
        return reverse('filme:login') #é a msm coisa que o redirect, mas essa function usa o reversed, quando a function pede uma resposta de LINK 
    
    
    

# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context["lista_filmes"] = lista_filmes
#     return render(request, "homefilmes.html", context)
#esse tipo é igual o exemplo de cima, é bom para coisas mais simples, mas com ctz vale mais a pena o class 

#def homepage(request):
#    return render(request, "homepage.html")
#caso queira usar o def para uma função mais simples como exibir que é esse caso pode usar o function, mas o mais "correto" é usar a class seguindo essa estrutura 
