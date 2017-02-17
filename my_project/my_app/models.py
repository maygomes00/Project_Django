from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

RACA_CHOICES = (
	('DOG', 'Dog'),
	('CAT', 'Cat'),
)

SEXO_CHOICES = (
	('MALE', 'Male'),
	('FEMALE', 'Female'),
)

class Animal(models.Model):
	name = models.CharField(max_length = 100)
	species = models.CharField(max_length = 50, choices = RACA_CHOICES)
	sex = models.CharField(max_length = 50, choices = SEXO_CHOICES)
	photo = models.ImageField(null = True)
	owner = models.ForeignKey('Client', null = True, related_name = 'animals')

	def __unicode__(self):
		return self.name

class Client(models.Model):
	name = models.CharField(max_length = 100)
	phone = models.CharField(max_length = 100)
	cpf = models.CharField(max_length = 11)
	address = models.ForeignKey('Address', null = True)
	user = models.OneToOneField(settings.AUTH_USER_MODEL)

	def __unicode__(self):
		return self.name

class Address(models.Model):
	street = models.CharField(max_length = 100)
	num = models.CharField(max_length = 100)
	district = models.CharField(max_length = 100)
	city = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.street + "," + " " + self.num + " " + "-" + " " + self.district + "," + " " + self.city
		
		

