from django.db import models
from datetime import datetime
# Create your models here.


class Prenda(models.Model):
	descripcion = models.CharField(max_length=50)
	precio = models.DecimalField(max_digits=5,decimal_places=2)
	talla = models.CharField(max_length=50)
	categoria = models.CharField(max_length=50)
	imagen_url = models.URLField(null=True,max_length=250)
	def __unicode__(self):
		return self.descripcion




