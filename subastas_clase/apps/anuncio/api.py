from django.db.models.fields import return_None
from django.http import HttpResponse
from django.template.context_processors import request
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.anuncio.models import Categoria, Anuncio
from apps.anuncio.serializers import CategoriaSerializer, AnuncioSerializer
from apps.usuario.models import Usuario


class CategoriaListaAPIView(APIView):
    def get(self,request,format=None):
        categorias = Categoria.objects.all()
        categoriasSerializer = CategoriaSerializer(categorias, many=True)
        return Response(categoriasSerializer.data)

    def post(self,request,format=None):
        categoriaSerializer = CategoriaSerializer(data=request.data)
        if categoriaSerializer.is_valid():
            categoriaSerializer.save()
            return Response(categoriaSerializer.data,status=status.HTTP_201_CREATED)
        return Response(categoriaSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoriaDetalleAPIView(APIView):
    def get(self,request,pk,format=None):
        categoria = get_object_or_404(Categoria,pk=pk)
        categoriaSerializer = CategoriaSerializer(categoria)
        if categoria:
            return Response(categoriaSerializer.data, status=status.HTTP_200_OK)
        return Response(categoriaSerializer.errors, status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk, format=None):
        categoria = get_object_or_404(Categoria,pk=pk)
        categoriaSerializer = CategoriaSerializer(categoria,data=request.data)
        if categoriaSerializer.is_valid():
            categoriaSerializer.save()
            return Response(categoriaSerializer.data,status=status.HTTP_200_OK)
        return Response(categoriaSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk, format=None):
        categoria = get_object_or_404(Categoria, pk=pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AnuncioListaAPIView(APIView):
    def get(self,request,format=None):
        anuncios = Anuncio.objects.all()
        anunciosSerializer = AnuncioSerializer(anuncios,many=True)
        return Response(anunciosSerializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
       anuncioSerializer = AnuncioSerializer(data=request.data)
       if anuncioSerializer.is_valid():
           anuncioSerializer.save()
           return Response(anuncioSerializer.data,status=status.HTTP_201_CREATED)
       return Response(anuncioSerializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AnuncioDetalleAPIView(APIView):
    def get(self,request,pk, format=None):
        anuncio = get_object_or_404(Anuncio,pk=pk)
        anuncioSerializer = AnuncioSerializer(anuncio)
        return Response(anuncioSerializer.data,status = status.HTTP_200_OK)

    def put(self,request,pk,format=None):
        anuncio = get_object_or_404(Anuncio,pk=pk)
        anuncioSerializer=AnuncioSerializer(anuncio,data=request.data)
        if anuncioSerializer.is_valid():
            anuncioSerializer.save()
            return Response(anuncioSerializer.data, status=status.HTTP_200_OK)
        return Response(anuncioSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk, format=None):
        anuncio=get_object_or_404(Anuncio,pk=pk)
        anuncio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)