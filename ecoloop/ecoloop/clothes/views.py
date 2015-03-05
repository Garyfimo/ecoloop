from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Prenda

# Create your views here.
def home(request):
	list_prenda = Prenda.objects.all()
	template = loader.get_template('ecoloop/index.html')
	context = RequestContext(request, {
		'list_prenda' : list_prenda,
		})
	#return render(request,'index.html')
	return HttpResponse(template.render(context))