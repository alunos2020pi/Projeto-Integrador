from django.urls import path
from ofertas import views


urlpatterns = [
    path('', views.index, name='index'),
    path('supermercados/', views.SupermercadoListView.as_view(), name='supermercados'),
    path('produtos/', views.ProdutoListView.as_view(), name='produtos'),
    path('ofertas/', views.Em_OfertaListView.as_view(), name='ofertas'),
]