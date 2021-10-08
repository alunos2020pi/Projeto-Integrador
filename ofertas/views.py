from django.shortcuts import render

# Create your views here.
from ofertas.models import Supermercado, Produto, Em_Oferta

def index(request):
    """Função view para a página inicial do site"""
    #Gera alguns contadores para os objetos principais
    num_super = Supermercado.objects.all().count()
    num_prod = Produto.objects.all().count()
    num_ofertas = Em_Oferta.objects.all().count()
    
    
    context = {
        'num_super': num_super,
        'num_prod': num_prod,
        'num_ofertas': num_ofertas,
    }
    
    #Renderiza o template index.html com os dados na variável context
    return render(request, 'index.html', context=context)
    