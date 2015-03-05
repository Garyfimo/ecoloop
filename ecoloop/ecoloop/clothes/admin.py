from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Prenda
# Register your models here.

@admin.register(Prenda)
class PrendaAdmin(admin.ModelAdmin):
	pass

class EcoloopAdminSite(AdminSite):
	site_header = "Ecoloop Administration"
	site_title = "Administration - Ecoloop"

admin_site = EcoloopAdminSite()
