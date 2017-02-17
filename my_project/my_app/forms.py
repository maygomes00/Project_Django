from django import forms
from django.contrib.auth.models import User
from .models import Client, Address, Animal

RACA_CHOICES = (
	('DOG', 'Dog'),
	('CAT', 'Cat'),
)

SEXO_CHOICES = (
	('MALE', 'Male'),
	('FEMALE', 'Female'),
)
		

class ClientForm(forms.Form):
	name = forms.CharField(max_length = 100)
	cpf = forms.CharField(max_length = 11)
	phone = forms.CharField(max_length = 100)
	street = forms.CharField(max_length = 100)
	num = forms.CharField(max_length = 100)
	district = forms.CharField(max_length = 100)
	city = forms.CharField(max_length = 100)
	email = forms.EmailField(max_length = 100)
	password = forms.CharField(max_length = 100, widget = forms.PasswordInput)


	def clean(self):
		cleaned_data = super(ClientForm, self).clean()

		try:
			if User.objects.filter(username = cleaned_data ['email']).count() > 0:
				self.add_error('email', 'Este email ja esta cadastrado')
		except Exception as e:
			raise e
		else:
			pass
		finally:
			pass

	def save(self):
		data = self.cleaned_data
		user = User.objects.create_user(username = data ['email'], email = data ['email'], password = data ['password'])

		address = Address(street = data ['street'], num = data ['num'], district = data ['district'], city = data ['city'])
		address.save()

		client = Client(name = data ['name'], phone = data ['phone'], cpf = data ['cpf'])
		client.user = user
		client.address = address
		client.save()
		return True	


class RegisterModelForm(forms.ModelForm):

	name = forms.CharField(max_length = 100)
	cpf = forms.CharField(max_length = 11)
	phone = forms.CharField(max_length = 100)
	street = forms.CharField(max_length = 100)
	num = forms.CharField(max_length = 100)
	district = forms.CharField(max_length = 100)
	city = forms.CharField(max_length = 100)
	email = forms.EmailField(max_length = 100)
	password = forms.CharField(max_length = 100, widget = forms.PasswordInput)

	class Meta:
		model = Client
		fields = ['name', 'cpf', 'phone']

	def clean(self):
		name = self.cleaned_data.get('name')
		cpf = self.cleaned_data.get('cpf')
		phone = self.cleaned_data.get('phone')
		street = self.cleaned_data.get('street')
		num = self.cleaned_data.get('num')
		district = self.cleaned_data.get('district')
		city = self.cleaned_data.get('city')
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')

		new_address = Address.objects.create(street = street, num = num, district = district, city = city)
		new_user = User.objects.create_user(username = email, email = email, password = password)

		self.cleaned_data['user'] = new_user
		self.cleaned_data['address'] = new_address

		return super(RegisterModelForm,self).clean()

class RegisterAnimalForm(forms.ModelForm):

	name = forms.CharField(max_length = 100)
	species = forms.ChoiceField(choices = RACA_CHOICES)
	sex = forms.ChoiceField(choices = SEXO_CHOICES)
	photo = forms.ImageField()
	

	class Meta:
		model = Animal
		fields = ['name', 'species', 'sex', 'photo', 'owner']

	def clean(self):
		name = self.cleaned_data.get('name')
		species = self.cleaned_data.get('species')
		sex = self.cleaned_data.get('sex')
		photo = self.cleaned_data.get('photo')


		new_animal = Animal.objects.create(name = name, species = species, sex = sex, photo = photo)
		
		

		return super(RegisterAnimalForm,self).clean()

class LoginForm(forms.Form):
	email = forms.EmailField(max_length = 100)
	password = forms.CharField(max_length = 100, widget = forms.PasswordInput)

	def clean(self):
		cleaned_data = super(LoginForm, self).clean()
		user = User.objects.get(username = cleaned_data ['email'])

		if user is not None:
			return cleaned_data

	
	
			


	

	
