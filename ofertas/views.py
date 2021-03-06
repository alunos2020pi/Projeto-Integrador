from django.shortcuts import render
from datetime import date
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.
from ofertas.models import Supermercado, Produto, Em_Oferta, Loja

def index(request):
	"""Função view para a página inicial do site"""
	#Gera alguns contadores para os objetos principais
	today = date.today()
	num_super = Supermercado.objects.all().count()
	num_prod = Produto.objects.all().count()
	num_ofertas = Em_Oferta.objects.filter(fim__gte=today).count()
    
    
	context = {
		'num_super': num_super,
		'num_prod': num_prod,
		'num_ofertas': num_ofertas,
	}
    
	#Renderiza o template index.html com os dados na variável context
	return render(request, 'index.html', context=context)

def about(request):
	"""Função view para a página sobre nós do site"""
	#Renderiza o template about.html
	return render(request, 'about.html')

from django.views import generic

class SupermercadoListView(generic.ListView):
	model = Supermercado

class ProdutoListView(generic.ListView):
	model = Produto

class Em_OfertaListView(generic.ListView):
	today = date.today()
	model = Em_Oferta
	queryset = Em_Oferta.objects.filter(fim__gte=today)
 
def ofertasporsuper(request, pk):
	"""Função view para a página ofertas por super"""
	today = date.today()
	super = Supermercado.objects.get(id=pk)
	ofertasporsuper = Em_Oferta.objects.filter(sm__id__exact=pk,fim__gte=today)
	lojas = Loja.objects.filter(sm__id__exact=pk)
	context = {
		'super': super,
		'ofertasporsuper': ofertasporsuper,
		'lojas': lojas,
	}
	#Renderiza o template index.html com os dados na variável context
	return render(request, 'ofertasporsuper.html', context=context)
    
def ondeencontrar(request, pk):
	"""Função view para a encontrar supermercados que possuem um produto específico em oferta"""
	today = date.today()
	produto = Produto.objects.get(id=pk)
	locais = Em_Oferta.objects.filter(pd__id__exact=pk, fim__gte=today)
	context = {
		'locais': locais,
		'produto': produto,
	}
	   
	#Renderiza o template ondeencontrar.html com os dados na variável context
	return render(request, 'ondeencontrar.html', context=context)
	
@method_decorator(login_required, name='dispatch')
class SupermercadoCreate(CreateView):
    model = Supermercado
    fields = ['nome', 'site']
	
    def form_valid(self, form):
        form.instance.informante = self.request.user
        form.instance.nome = form.instance.nome.title()
        return super().form_valid(form)		

@method_decorator(login_required, name='dispatch')
class LojaCreate(CreateView):
    model = Loja
    fields = ['sm', 'nome', 'lograd', 'num', 'bairro', 'cidade', 'estado', 'cep']
	
    def form_valid(self, form):
        form.instance.informante = self.request.user
        form.instance.nome = form.instance.nome.title()
        form.instance.lograd = form.instance.lograd.title()
        form.instance.bairro = form.instance.bairro.title()
        form.instance.cidade = form.instance.cidade.title()		
        return super().form_valid(form)		
	
@method_decorator(login_required, name='dispatch')
class ProdutoCreate(CreateView):
    model = Produto
    fields = ['desc', 'marca', 'qtd', 'unid', 'obs']
	
    def form_valid(self, form):
        form.instance.informante = self.request.user
        form.instance.desc = form.instance.desc.title()
        form.instance.marca = form.instance.marca.title()		
        return super().form_valid(form)		

@method_decorator(login_required, name='dispatch')	
class Em_OfertaCreate(CreateView):
    model = Em_Oferta
    fields = ['sm', 'pd', 'preco', 'inicio', 'fim', 'obs', 'fonte']
	
    def form_valid(self, form):
        form.instance.informante = self.request.user
        return super().form_valid(form)

class MeusSupermercadosCadastradosListView(LoginRequiredMixin,generic.ListView):
    model = Supermercado
    template_name = 'ofertas/meus_super_cadast_list_user.html'

    def get_queryset(self):
        return Supermercado.objects.filter(informante=self.request.user)
		
class SupermercadoUpdate(LoginRequiredMixin, UpdateView):
	model = Supermercado
	fields = ['nome', 'site']
	

class SupermercadoDelete(LoginRequiredMixin, DeleteView):
	model = Supermercado
	success_url = reverse_lazy('supermercados')
	
class MinhasLojasCadastradasListView(LoginRequiredMixin,generic.ListView):
    model = Loja
    template_name = 'ofertas/minhas_lojas_cadast_list_user.html'

    def get_queryset(self):
        return Loja.objects.filter(informante=self.request.user)

class LojaUpdate(LoginRequiredMixin, UpdateView):
	model = Loja
	fields = ['sm', 'nome', 'lograd', 'num', 'bairro', 'cidade', 'estado', 'cep']

class LojaDelete(LoginRequiredMixin, DeleteView):
	model = Loja
	success_url = reverse_lazy('supermercados')

class MeusProdutosCadastradosListView(LoginRequiredMixin,generic.ListView):
    model = Produto
    template_name = 'ofertas/meus_prod_cadast_list_user.html'

    def get_queryset(self):
        return Produto.objects.filter(informante=self.request.user)

class ProdutoUpdate(LoginRequiredMixin, UpdateView):
	model = Produto
	fields = ['desc', 'marca', 'qtd', 'unid', 'obs']

class ProdutoDelete(LoginRequiredMixin, DeleteView):
	model = Produto
	success_url = reverse_lazy('produtos')

class MinhasOfertasCadastradasListView(LoginRequiredMixin,generic.ListView):
    model = Em_Oferta
    template_name = 'ofertas/minhas_ofertas_cadast_list_user.html'

    def get_queryset(self):
        return Em_Oferta.objects.filter(informante=self.request.user)

class Em_OfertaUpdate(LoginRequiredMixin, UpdateView):
	model = Em_Oferta
	fields = ['sm', 'pd', 'preco', 'inicio', 'fim', 'obs', 'fonte']	

class Em_OfertaDelete(LoginRequiredMixin, DeleteView):
	model = Em_Oferta
	success_url = reverse_lazy('ofertas')

def minhascontrib(request):
	"""Função view para a página Minhas Contribuições"""
	#Renderiza o template about.html
	return render(request, 'minhas_contrib.html')			