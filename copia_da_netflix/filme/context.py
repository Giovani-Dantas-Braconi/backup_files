#arquivo para adicionar novos context 
#criar todas as variaveis que todas as paginas HTML terão acesso 

from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[:8]
    if lista_filmes:
        filmes_destaque = lista_filmes[0]
    else: 
        filmes_destaque = None
    return {"lista_filmes_recentes":lista_filmes, "filmes_destaque": filmes_destaque}  



def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[:8]
    return {"lista_filmes_emalta":lista_filmes}
