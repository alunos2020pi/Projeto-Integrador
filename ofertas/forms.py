from django.forms import ModelForm

from ofertas.models import Supermercado, Loja, Produto, Em_oferta

class AdicionaSuper(ModelForm):
    class Meta:
        model = Supermercado
        fields = ['nome', 'site']

class AdicionaLoja(ModelForm):
    class Meta:
        model = Loja
        fields = ['sm', 'nome', 'lograd', 'num', 'bairro', 'cidade', 'estado', 'cep']
		
class AdicionaProduto(ModelForm):
    class Meta:
        model = Produto	
        fields = ['desc', 'marca', 'qtd', 'unid', 'obs']
		
class AdicionaEm_Oferta(ModelForm):
    class Meta:
        model = Em_Oferta	
        fields = ['sm', 'pd', 'preco', 'inicio', 'fim', 'obs']