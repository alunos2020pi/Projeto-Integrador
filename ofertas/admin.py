from django.contrib import admin

# Register your models here.

from ofertas.models import Supermercado, Produto, Em_Oferta, Loja

@admin.register(Supermercado)
class SupermercadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site','informante')

@admin.register(Loja)
class LojaAdmin(admin.ModelAdmin):
    list_display = ('sm','nome','lograd','num','bairro','cidade','estado','cep','informante')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('desc', 'marca', 'qtd', 'unid', 'obs','informante')

@admin.register(Em_Oferta)
class Em_OfertaAdmin(admin.ModelAdmin):
    list_display = ('sm', 'pd', 'preco', 'inicio', 'fim', 'fonte','informante')