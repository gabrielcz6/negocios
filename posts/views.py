# posts/views.py
from rest_framework import generics,permissions
from .models import Post,Carrera,Proyecto
from .serializers import PostSerializer,CarreraSerializer,ProyectoSerializer
from .permissions import IsAuthorOrReadOnly # new


class PostList(generics.ListCreateAPIView):
   #permission_classes = (IsAuthorOrReadOnly,)  # Un permiso customizado
   permission_classes = (permissions.IsAuthenticated,) # para permiso ver solo cuando esta autentificado
   queryset = Post.objects.all()
   serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
   permission_classes = (permissions.IsAuthenticated,)
   #permission_classes = (IsAuthorOrReadOnly,) # new
   queryset = Post.objects.all()
   serializer_class = PostSerializer   

class CarreraList(generics.ListCreateAPIView):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class CarreraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer   

class ProyectoList(generics.ListCreateAPIView):
    queryset = Proyecto.objects.all()  # Obtener todos los proyectos
    serializer_class = ProyectoSerializer  # Usar el serializador que creamos

class ProyectoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proyecto.objects.all()  # Obtener un proyecto en particular
    serializer_class = ProyectoSerializer  # Usar el serializador que creamos
   