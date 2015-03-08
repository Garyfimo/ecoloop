from django.shortcuts import render


from .models import Prenda

# Create your views here.
def home(request):
	list_prenda = Prenda.objects.all()
	context = {
		'list_prenda' : list_prenda,
		}
	return render(request,'ecoloop/index.html',context)
