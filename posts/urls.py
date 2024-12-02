# posts/urls.py
from django.urls import path
from .views import PostList, PostDetail,CarreraList,CarreraDetail,ProyectoDetail,ProyectoList



urlpatterns = [

 path('<int:pk>/', PostDetail.as_view()),
 path('', PostList.as_view()),
 path('carreras/', CarreraList.as_view(), name='carrera-list'),  # Para listar o crear carreras
 path('carreras/<int:pk>/', CarreraDetail.as_view(), name='carrera-detail'),  # Para ver, actualizar o eliminar carrera específica
 path('proyectos/', ProyectoList.as_view(), name='proyecto-list'),  # Ver todos los proyectos o crear uno
 path('proyectos/<int:pk>/', ProyectoDetail.as_view(), name='proyecto-detail'),  # Ver, editar o eliminar un proyecto

]