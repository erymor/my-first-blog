from django.contrib import admin
from .models import Post

# Nombre: djangogirls/miblog/admin.py

#Registra nuestro objeto Post en el administrador
# de Django para poder consultar o actualiza información del o de los Post's.

admin.site.register(Post)
