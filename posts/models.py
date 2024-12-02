from django.db import models

# Create your models here.
# posts/models.py
from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
         id = models.BigAutoField(primary_key=True)  # Usando BigAutoField
         author = models.ForeignKey(User, on_delete=models.CASCADE)
         title = models.CharField(max_length=50)
         body = models.TextField()
         created_at = models.DateTimeField(auto_now_add=True)
         updated_at = models.DateTimeField(auto_now=True)
         def __str__(self):
            return self.title
         
class Carrera(models.Model):
    id = models.BigAutoField(primary_key=True)  # Usando BigAutoField
    nombre = models.CharField(max_length=255)  # Nombre de la carrera (e.g., Ingeniería Informática)
    descripcion = models.TextField()  # Descripción de la carrera
    

    def __str__(self):
        return self.nombre      

class Proyecto(models.Model):
    id = models.BigAutoField(primary_key=True)    
    nombre_proyecto = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)  # Subir imagen a una carpeta 'proyectos'

    def __str__(self):
        return self.nombre_proyecto       