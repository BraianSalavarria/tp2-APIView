from django.urls import path

from apps.anuncio.api import CategoriaListaAPIView, CategoriaDetalleAPIView, AnuncioListaAPIView, AnuncioDetalleAPIView

app_name='anuncio'

urlpatterns = [
    path('api-view/categorias/', CategoriaListaAPIView.as_view()),
    path('api-view/categorias/<int:pk>/',CategoriaDetalleAPIView.as_view()),
    path('api-view/anuncios/',AnuncioListaAPIView.as_view()),
    path('api-view/anuncios/<int:pk>/',AnuncioDetalleAPIView.as_view())
]