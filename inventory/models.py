from django.db import models

class Item(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	amount = models.IntegerField()
	availability = models.IntegerField(default=0)

class Supplier(models.Model):
	name = models.CharField(max_length = 200)
	location = models.CharField(max_length = 200)
	ratings = models.IntegerField(default=0)