from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Prenda, Genero, Ecoloop
# Register your models here.

@admin.register(Prenda)
class PrendaAdmin(admin.ModelAdmin):
	list_display = ('descripcion','talla','genero','precio','was_published_recently')
	list_filter = ['genero','categoria']
	#search_fields = ['categoria','genero']

#@admin.register(Genero)
#class GeneroAdmin(admin.ModelAdmin):
#	pass

@admin.register(Ecoloop)
class EcoloopAdmin(admin.ModelAdmin):
	pass