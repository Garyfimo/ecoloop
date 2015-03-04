from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from clothes.models import Clothes

# Create your views here.
def home(request):
	list_clothes = Clothes.objects.all()
	for l in list_clothes:
		print l.description
	template = loader.get_template('ecoloop/index.html')
	context = RequestContext(request, {
		'list_clothes' : list_clothes,
		})
	#return render(request,'index.html')
	return HttpResponse(template.render(context))