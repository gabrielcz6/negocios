# posts/admin.py
from django.contrib import admin
from .models import Post,Carrera,Proyecto



admin.site.register(Post)
admin.site.register(Carrera)
admin.site.register(Proyecto)
