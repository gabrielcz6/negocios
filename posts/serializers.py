# posts/serializers.py


from rest_framework import serializers
from .models import Post,Carrera,Proyecto

class PostSerializer(serializers.ModelSerializer):
   class Meta:
    fields = ('id', 'author', 'title', 'body', 'created_at',)
    model = Post

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = ['id', 'nombre', 'descripcion', 'duracion', 'fecha_creacion']

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ['id', 'nombre_proyecto', 'descripcion', 'imagen']        