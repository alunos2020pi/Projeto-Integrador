from django.urls import path
from ofertas import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('supermercados/', views.SupermercadoListView.as_view(), name='supermercados'),
    path('produtos/', views.ProdutoListView.as_view(), name='produtos'),
    path('ofertas/', views.Em_OfertaListView.as_view(), name='ofertas'),
    path('ofertasporsuper/<int:pk>', views.ofertasporsuper, name='ofertasporsuper'),
    path('ondeencontrar/<int:pk>', views.ondeencontrar, name='ondeencontrar'),
	path('supermercado/create/', views.SupermercadoCreate.as_view(), name='supermercado-create'),
	path('loja/create/', views.LojaCreate.as_view(), name='loja-create'),
	path('produto/create/', views.ProdutoCreate.as_view(), name='produto-create'),
	path('em_oferta/create/', views.Em_OfertaCreate.as_view(), name='em_oferta-create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)