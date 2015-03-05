from django.contrib import admin
from .models import Prenda
# Register your models here.

@admin.register(Prenda)
class PrendaAdmin(admin.ModelAdmin):
	pass
