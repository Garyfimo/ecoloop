from django.shortcuts import render


from .models import Prenda, Genero, Ecoloop

# Create your views here.
def home(request):
	genero = Genero.objects.get(descripcion="Masculino")
	list_prenda = genero.prenda_set.all()[0:8]
	context = {
		'list_prenda' : list_prenda,
		'is_active' : "hombres", 
		}
	return render(request,'ecoloop/index.html',context)

def mujeres(request):
	genero = Genero.objects.get(descripcion="Femenino")
	list_prenda = genero.prenda_set.all()[0:8]
	context = {
		'list_prenda' : list_prenda,
		'is_active' : "mujeres", 
		}
	return render(request,'ecoloop/mujeres.html',context)

def ecoloop(request):
	ecoloop = Ecoloop.objects.get(pk=1)
	context = {
		'ecoloop' : ecoloop,
		'is_active' : "ecoloop", 
		}
	return render(request,'ecoloop/ecoloop.html',context)

def noticias(request):
	context = {
		'is_active' : "noticias", 
		}
	return render(request,'ecoloop/news.html',context)

def contacto(request):
	context = {
		'is_active' : "contacto", 
		}
	return render(request,'ecoloop/contact.html',context)

