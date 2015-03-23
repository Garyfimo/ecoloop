import datetime

from django.db import models
from django.utils import timezone
# Create your models here.


class Prenda(models.Model):
	descripcion = models.CharField(max_length=50)
	precio = models.DecimalField(max_digits=5,decimal_places=2)
	talla = models.CharField(max_length=50)
	categoria = models.CharField(max_length=50)
	imagen_url = models.URLField(null=True,max_length=250)
	pub_date = models.DateTimeField('date published',auto_now_add=True,auto_now=False)
	def __unicode__(self):
		return self.descripcion
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=0.8)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'






