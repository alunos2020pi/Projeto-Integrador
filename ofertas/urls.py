from django.urls import path
from ofertas import views


urlpatterns = [
    path('', views.index, name='index'),
]