from django.shortcuts import render


from .models import Prenda

# Create your views here.
def home(request):
	list_prenda = Prenda.objects.all()[0:8]
	context = {
		'list_prenda' : list_prenda,
		'is_active' : "hombres", 
		}
	return render(request,'ecoloop/index.html',context)

def mujeres(request):
	context = {
		'is_active' : "mujeres", 
		}
	return render(request,'ecoloop/mujeres.html',context)

def ecoloop(request):
	context = {
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

