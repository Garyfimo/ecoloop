from django.shortcuts import render


from .models import Prenda

# Create your views here.
def home(request):
	list_prenda = Prenda.objects.all()
	context = {
		'list_prenda' : list_prenda,
		}
	return render(request,'ecoloop/index.html',context)

def mujeres(request):
	return render(request,'ecoloop/mujeres.html')

def ecoloop(request):
	return render(request,'ecoloop/ecoloop.html')

def noticias(request):
	return render(request,'ecoloop/news.html')

def contacto(request):
	return render(request,'ecoloop/contact.html')

