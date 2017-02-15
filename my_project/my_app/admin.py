from django.contrib import admin
from .models import Animal
from .models import Client
from .models import Address

# Register your models here.

class AnimalInLine(admin.TabularInline):
	model = Animal

class ClientAdmin(admin.ModelAdmin):
	list_display = ('name', 'cpf')
	inlines = [AnimalInLine,]

class AnimalInfo(admin.ModelAdmin):
	list_display = ('name', 'species', 'owner')


admin.site.register(Animal, AnimalInfo)
admin.site.register(Client, ClientAdmin)
admin.site.register(Address)
		