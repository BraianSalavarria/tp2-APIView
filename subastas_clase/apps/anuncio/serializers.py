from rest_framework import serializers
from apps.anuncio.models import Categoria, Anuncio
from apps.usuario.models import Usuario


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = [
            'id',
            'nombre',
            'activa',
        ]

class AnuncioSerializer(serializers.ModelSerializer):
    categorias = serializers.PrimaryKeyRelatedField(many=True, queryset=Categoria.objects.all())
    publicado_por = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())

    class Meta:
        model = Anuncio
        fields = [
            'id',
            'titulo',
            'descripcion',
            'precio_inicial',
            'imagen',
            'fecha_inicio',
            'fecha_fin',
            'activo',
            'categorias',
            'publicado_por',
            'oferta_ganadora'
        ]