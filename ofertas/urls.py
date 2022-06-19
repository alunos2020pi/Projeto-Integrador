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
	path('meussuper/', views.MeusSupermercadosCadastradosListView.as_view(), name='meussuper'),
	path('supermercado/<int:pk>/update/', views.SupermercadoUpdate.as_view(), name='supermercado-update'),
	path('supermercado/<int:pk>/delete/', views.SupermercadoDelete.as_view(), name='supermercado-delete'),
	path('minhaslojas/', views.MinhasLojasCadastradasListView.as_view(), name='minhaslojas'),
	path('loja/<int:pk>/update/', views.LojaUpdate.as_view(), name='loja-update'),
	path('loja/<int:pk>/delete/', views.LojaDelete.as_view(), name='loja-delete'),
	path('meusprod/', views.MeusProdutosCadastradosListView.as_view(), name='meusprod'),
	path('produto/<int:pk>/update/', views.ProdutoUpdate.as_view(), name='produto-update'),	
	path('produto/<int:pk>/delete/', views.ProdutoDelete.as_view(), name='produto-delete'),	
	path('minhasofertas/', views.MinhasOfertasCadastradasListView.as_view(), name='minhasofertas'),	
	path('oferta/<int:pk>/update/', views.Em_OfertaUpdate.as_view(), name='oferta-update'),
	path('oferta/<int:pk>/delete/', views.Em_OfertaDelete.as_view(), name='oferta-delete'),	
    path('minhascontrib/', views.minhascontrib, name='minhascontrib')		
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)