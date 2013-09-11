from django.db import models

class Person(models.Model):
	name = models.CharField(max_length=100, blank=True)
	gtID = models.IntegerField(primary_key=True)
	
	def __str__(self):
		return self.name + " " + str(self.gtID)
	
	def __unicode(self):
		return self.__str__()

class Item(models.Model):
	title = models.CharField(max_length=100)
	code = models.IntegerField(primary_key=True)
	description = models.CharField(max_length=200, blank=True)
	image = models.ImageField(upload_to='items', blank=True)
	checked_out = models.BooleanField(default=False)
	
	#if not checked_out, last person (or None) to check out
	#if checked_out, current Person 
	owner = models.ForeignKey(Person,null=True, blank=True)

	def __str__(self):
		return self.title
	
	def __unicode(self):
		return self.__str__()

class Book(Item):
	author = models.CharField(max_length=100)
