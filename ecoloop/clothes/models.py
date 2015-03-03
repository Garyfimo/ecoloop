from django.db import models

# Create your models here.
class Clothes(models.Model):
	description = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=3, decimal_places=2)
	size_id = models.ForeignKey('Size')	
	category_id = models.ForeignKey('Category')	

	def __unicode__(self):
		return self.description


class Size(models.Model):
	description = models.CharField(max_length=50)
	def __unicode__(self):
		return self.description

class Category(models.Model):
	description = models.CharField(max_length=50)
	def __unicode__(self):
		return self.description
